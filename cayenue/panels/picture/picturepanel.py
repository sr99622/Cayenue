#/********************************************************************
# Cayenue/cayenue/panels/picture/picturepanel.py 
#
# Copyright (c) 2026  Stephen Rhodes
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#*********************************************************************/

import os
from loguru import logger
from PyQt6.QtWidgets import QGridLayout, QWidget, \
    QLabel, QAbstractItemView, QAbstractItemView, \
    QApplication, QTreeView, QMenu, QMessageBox
from PyQt6.QtGui import QFileSystemModel, QAction, QColorConstants
from PyQt6.QtCore import Qt, QFileInfo, QDateTime, \
    QDate, QTime, QStandardPaths
from cayenue.components.directoryselector import DirectorySelector
from cayenue.panels.file import FileControlPanel, FileSortProxy
from cayenue.components import Progress, InfoDialog
from pathlib import Path
import traceback

class PicTreeView(QTreeView):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw

    def keyPressEvent(self, event):

        if not self.isVisible():
            return super().keyPressEvent(event)

        pass_through = True

        match event.key():
            case Qt.Key.Key_Return:
                if self.mw.picturePanel.model.isReadOnly():
                    pass_through = False
                    if player := self.mw.filePanel.getCurrentlyPlayingFile():
                        self.mw.closeAllStreams()
                    proxy_index = self.currentIndex()
                    if proxy_index.isValid():
                        model_index = self.mw.picturePanel.proxy.mapToSource(proxy_index)
                        fileInfo = self.mw.picturePanel.model.fileInfo(model_index)
                        if fileInfo.isFile():
                            self.mw.picturePanel.playVideo()
                        else:
                            if self.isExpanded(proxy_index):
                                self.collapse(proxy_index)
                            else:
                                self.expand(proxy_index)
            case Qt.Key.Key_Escape:
                if player := self.mw.filePanel.getCurrentlyPlayingFile():
                    self.mw.closeAllStreams()
                    pass_through = False
                else:
                    self.mw.glWidget.buffer.fill(QColorConstants.Black)
                    self.mw.glWidget.update()
            case Qt.Key.Key_Space:
                if player := self.mw.filePanel.getCurrentlyPlayingFile():
                    player.togglePaused()
            case Qt.Key.Key_Left:
                self.mw.filePanel.rewind()
                pass_through = False
            case Qt.Key.Key_Right:
                self.mw.filePanel.fastForward()
                pass_through = False
            case Qt.Key.Key_F1:
                self.mw.picturePanel.onMenuInfo()
            case Qt.Key.Key_F2:
                self.mw.picturePanel.onMenuRename()
            case Qt.Key.Key_Delete:
                self.mw.picturePanel.onMenuRemove()

        if pass_through:
            return super().keyPressEvent(event)
        
    def showCurrentFile(self):
        try:
            if self.mw.settings_profile != "Reader":
                return
            proxy_index = self.currentIndex()
            if proxy_index.isValid():
                model_index = self.mw.picturePanel.proxy.mapToSource(proxy_index)
                info = self.mw.picturePanel.model.fileInfo(model_index)
                if info.isFile() and self.mw.picturePanel.model.isReadOnly():
                    self.mw.glWidget.drawFile(info.absoluteFilePath())
                
        except Exception as ex:
            logger.error(f"PicturePanel showCurrentFile exception: {ex}")

    def currentChanged(self, newIndex, oldIndex):
        if newIndex.isValid():
            self.showCurrentFile()
            self.scrollTo(newIndex)

class PicturePanel(QWidget):                
    def __init__(self, mw):
        super().__init__(mw)
        self.mw = mw
        self.geometryKey = "PictureBrowseDialog/geometry"
        self.splitKey = "PictureBrowseDialog/splitSettings"
        self.headerKey = "PictureBrowseDialog/header"
        self.positionInitialized = False
        self.setWindowTitle("Event Browser")
        self.expandedPaths = []
        self.loadedCount = 0
        self.restorationPath = None
        self.restorationHeader = None
        self.verticalScrollBarPosition = 0
        self.control = FileControlPanel(mw, self)
        self.progress = Progress(mw)
        self.dlgInfo = InfoDialog(mw)

        tmp_dir = QStandardPaths.standardLocations(QStandardPaths.StandardLocation.PicturesLocation)[0]
        if self.mw.parent_window:
            tmp_dir = self.mw.parent_window.settingsPanel.storage.dirPictures.text()
        self.dirPictures = DirectorySelector(mw, self.mw.settingsPanel.storage.pictureKey, "", tmp_dir)
        self.picture_dir = self.dirPictures.text()
        self.dirPictures.signals.dirChanged.connect(self.dirChanged)

        self.model = QFileSystemModel(mw)
        self.tree = PicTreeView(mw)

        self.proxy = FileSortProxy()
        self.proxy.setSourceModel(self.model)
        self.proxy.setDynamicSortFilter(True)

        self.tree.setModel(self.proxy)
        self.model.fileRenamed.connect(self.onFileRenamed)
        self.model.directoryLoaded.connect(self.loaded)

        self.tree.doubleClicked.connect(self.treeDoubleClicked)
        if data := self.mw.settings.value(self.headerKey):
            self.tree.header().restoreState(data)
        self.tree.update()
        self.tree.header().sectionResized.connect(self.headerChanged)
        self.tree.header().sectionMoved.connect(self.headerChanged)
        self.tree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.showContextMenu)

        self.dirChanged(self.dirPictures.text())

        pnlTree = QWidget()
        lytTree = QGridLayout(pnlTree)
        lytTree.addWidget(self.dirPictures,       0, 0, 1, 1)
        lytTree.addWidget(self.tree,              1, 0, 1, 1)
        lytTree.addWidget(self.progress,          2, 0, 1, 1)
        lytTree.addWidget(QLabel(),               3, 0, 1, 1)
        lytTree.addWidget(self.control,  4, 0, 1, 1)

        lytMain = QGridLayout(self)
        lytMain.addWidget(pnlTree)
        lytMain.setContentsMargins(0, 0, 0, 0)

        self.menu = QMenu("Context Menu", self)
        self.remove = QAction("Delete", self)
        self.rename = QAction("Rename", self)
        self.info = QAction("Info", self)
        self.remove.triggered.connect(self.onMenuRemove)
        self.rename.triggered.connect(self.onMenuRename)
        self.info.triggered.connect(self.onMenuInfo)
        self.menu.addAction(self.remove)
        self.menu.addAction(self.rename)
        self.menu.addAction(self.info)

    def headerChanged(self, a, b, c):
        self.mw.settings.setValue(self.headerKey, self.tree.header().saveState())

    def closeEvent(self, event):
        self.mw.settings.setValue(self.geometryKey, self.geometry())
        return super().closeEvent(event)

    def showEvent(self, event):
        if rect := self.mw.settings.value(self.geometryKey):
            if rect.width() and rect.height():
                self.setGeometry(rect)
                self.positionInitialized = True
        return super().showEvent(event)
    
    def splitterMoved(self, pos, index):
        self.mw.settings.setValue(self.splitKey, self.split.saveState())

    def filenameToQDateTime(self, filename):
        # file start times may be inaccurate on samba, use filename instead
        filename = Path(filename).stem
        year = int(filename[0:4])
        month = int(filename[4:6])
        date = int(filename[6:8])
        hour = int(filename[8:10])
        minute = int(filename[10:12])
        second = int(filename[12:14])
        qdate = QDate(year, month, date)
        qtime = (QTime(hour, minute, second))
        return QDateTime(qdate, qtime)
    
    def searchFiles(self, target, dir):
        try:
            alarm_buffer_size = self.mw.settingsPanel.alarm.spnBufferSize.value()
            files = os.listdir(dir)
            for file in files:
                file_info = QFileInfo(str(Path(dir) / file))
                start = self.filenameToQDateTime(file).addSecs(-alarm_buffer_size)
                finish = file_info.lastModified()
                if (target >= start and target <= finish):
                    return file
            return None
        except Exception as ex:
            logger.error(f"PicturePanel searchFile exception: {ex}")

    def calculateTargetPct(self, target, file, dir):
        alarm_buffer_size = self.mw.settingsPanel.alarm.spnBufferSize.value()
        start = self.filenameToQDateTime(file).addSecs(-alarm_buffer_size)
        finish = QFileInfo(str(Path(dir) / file)).lastModified()
        numerator = start.secsTo(target)
        denominator = start.secsTo(finish)
        if denominator > 0:
            pct = float(numerator / denominator)
            if pct > 0.98:
                pct = 0.95
        else:
            pct = 0.95
        return pct

    def playVideo(self):
        try:
            uri = self.mw.filePanel.getCurrentFileURI()
            if player := self.mw.pm.getPlayer(uri):
                player.togglePaused()
                self.control.setBtnPlay()
                return

            alarm_buffer_size = self.mw.settingsPanel.alarm.spnBufferSize.value()
            proxy_index = self.tree.currentIndex()
            if proxy_index.isValid():
                model_index = self.proxy.mapToSource(proxy_index)
                pic_info = self.model.fileInfo(model_index)
                if pic_info.isFile():
                    target = self.filenameToQDateTime(pic_info.fileName())
                    dir = Path(self.mw.filePanel.dirArchive.txtDirectory.text()) / str(pic_info.absoluteDir().dirName())

                    # everything is approximate, so give the algorithm a couple chances to find near miss
                    found = False
                    if file := self.searchFiles(target, dir):
                        found = True
                    else:
                        fuzz = target.addSecs(-alarm_buffer_size)
                        if file := self.searchFiles(fuzz, dir):
                            target = fuzz
                            found = True
                        else:
                            fuzz = target.addSecs(alarm_buffer_size)
                            if file := self.searchFiles(fuzz, dir):
                                target = fuzz
                                found = True

                    if not found:
                        return
                    
                    self.selectFileInFilePanelTree(str(dir), file)
                    pct = self.calculateTargetPct(target, file, dir)
                    vid_info = QFileInfo(os.path.join(dir, file))
                    if player := self.mw.pm.getPlayer(vid_info.absoluteFilePath()):
                        player.seek(pct)
                    else:
                        self.mw.closeAllStreams()
                        self.mw.playMedia(vid_info.absoluteFilePath(), file_start_from_seek=pct)
                        self.mw.glWidget.focused_uri = vid_info.absoluteFilePath()

        except Exception as ex:
            logger.error(f'Event browser exception: {ex}')
            logger.debug(traceback.format_exc())

    def selectFileInFilePanelTree(self, path, filename):
        tree = self.mw.filePanel.tree
        model = self.mw.filePanel.model
        if model_camera_idx := model.index(path):
            if model_camera_idx.isValid():
                proxy_camera_idx = self.mw.filePanel.proxy.mapFromSource(model_camera_idx)
                if not tree.isExpanded(proxy_camera_idx):
                    tree.setExpanded(proxy_camera_idx, True)
                if model_file_idx := model.index(os.path.join(path, filename)):
                    if model_file_idx.isValid():
                        proxy_file_idx = self.mw.filePanel.proxy.mapFromSource(model_file_idx)
                        tree.setCurrentIndex(proxy_file_idx)
                        tree.scrollTo(proxy_file_idx, QAbstractItemView.ScrollHint.PositionAtCenter)

    def loaded(self, path):
        self.loadedCount += 1
        self.tree.sortByColumn(1, Qt.SortOrder.AscendingOrder)
        for i in range(self.model.rowCount(self.model.index(path))):
            idx = self.model.index(i, 0, self.model.index(path))
            if idx.isValid():
                if self.model.filePath(idx) in self.expandedPaths:
                    self.tree.setExpanded(idx, True)

        if len(self.expandedPaths):
            if self.loadedCount == len(self.expandedPaths) + 1:
                if self.verticalScrollBarPosition:
                    QApplication.processEvents()
                    self.tree.verticalScrollBar().setValue(self.verticalScrollBarPosition)
                self.expandedPaths.clear()
                self.restoreSelectedPath()
        else:
            self.restoreSelectedPath()

    def restoreSelectedPath(self):
        if self.restorationPath:
            model_idx = self.model.index(self.restorationPath)
            if model_idx.isValid():
                proxy_idx = self.proxy.mapFromSource(model_idx)
                self.tree.setCurrentIndex(proxy_idx)
            self.restorationPath = None

    def refresh(self):
        try:
            self.loadedCount = 0
            self.expandedPaths = []
            proxy_idx = self.tree.currentIndex()
            if proxy_idx.isValid():
                model_idx = self.proxy.mapToSource(proxy_idx)
                self.restorationPath = self.model.filePath(model_idx)
            path = self.dirPictures.txtDirectory.text()
            self.model.sort(0)
            for i in range(self.model.rowCount(self.model.index(path))):
                model_idx = self.model.index(i, 0, self.model.index(path))
                if model_idx.isValid():
                    proxy_idx = self.proxy.mapFromSource(model_idx)
                    if self.tree.isExpanded(proxy_idx):
                        self.expandedPaths.append(self.model.filePath(model_idx))
            self.verticalScrollBarPosition = self.tree.verticalScrollBar().value()
            self.restorationHeader = self.tree.header().saveState()
            self.proxy.setSourceModel(None)
            self.model = QFileSystemModel()
            self.model.setRootPath(path)
            self.model.fileRenamed.connect(self.onFileRenamed)
            self.model.directoryLoaded.connect(self.loaded)
            self.proxy.setSourceModel(self.model)
            self.tree.setModel(self.proxy)
            self.tree.setRootIndex(self.proxy.mapFromSource(self.model.index(path)))
            self.restoreSelectedPath()
            if self.restorationHeader:
                self.tree.header().restoreState(self.restorationHeader)

        except Exception as ex:
            logger.error(f"PicturePanel refresh exception: {ex}")

    def dirChanged(self, path):
        if len(path) > 0:
            self.picture_dir = path
            self.model.setRootPath(path)
            self.tree.setRootIndex(self.proxy.mapFromSource(self.model.index(self.picture_dir)))

    def treeDoubleClicked(self, proxy_index):
        if proxy_index.isValid():
            model_index = self.proxy.mapToSource(proxy_index)
            fileInfo = self.model.fileInfo(model_index)
            if fileInfo.isDir():
                self.tree.setExpanded(proxy_index, self.tree.isExpanded(proxy_index))
            else:
                if player := self.mw.filePanel.getCurrentlyPlayingFile():
                    self.mw.closeAllStreams()
                self.playVideo()

    def onMediaStarted(self, duration):
        if self.mw.tab.currentIndex() == 1:
            self.tree.setFocus()
        self.control.setBtnPlay()
        self.control.setBtnMute()
        self.control.setSldVolume()

    def onMediaStopped(self, uri):
        self.control.setBtnPlay()
        self.progress.duration = 0
        self.progress.updateProgress(0.0)
        self.progress.lblDuration.setText("0:00")
        # not relavent to camera playback
        self.tree.showCurrentFile()

    def onMediaProgress(self, pct, uri):
        if player := self.mw.pm.getPlayer(uri):
            player.file_progress = pct
            self.progress.updateDuration(player.duration())

        #if pct >= 0.0 and pct <= 1.0 and uri == self.mw.glWidget.focused_uri:
        if pct >= 0.0 and pct <= 1.0:
            self.progress.updateProgress(pct)

    def showContextMenu(self, pos):
        proxy_index = self.tree.indexAt(pos)
        if proxy_index.isValid():
            model_index = self.proxy.mapToSource(proxy_index)
            fileInfo = self.model.fileInfo(model_index)
            if fileInfo.isFile():
                self.menu.exec(self.mapToGlobal(pos))

    def onMenuRemove(self):
        proxy_index = self.tree.currentIndex()
        if proxy_index.isValid():
            ret = QMessageBox.warning(self, "Cayenue",
                                        "You are about to ** PERMANENTLY ** delete this file.\n"
                                        "Are you sure you want to continue?",
                                        QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

            if ret == QMessageBox.StandardButton.Ok:
                try:
                    proxy_idxAbove = self.tree.indexAbove(proxy_index)
                    proxy_idxBelow = self.tree.indexBelow(proxy_index)

                    model_index = self.proxy.mapToSource(proxy_index)
                    self.model.remove(model_index)
                    
                    resolved = False
                    if proxy_idxAbove.isValid():
                        model_idxAbove = self.proxy.mapToSource(proxy_idxAbove)
                        if os.path.isfile(self.model.filePath(model_idxAbove)):
                            self.tree.setCurrentIndex(proxy_idxAbove)
                            resolved = True
                    if not resolved:
                        if proxy_idxBelow.isValid():
                            model_idxBelow = self.proxy.mapToSource(proxy_idxBelow)
                            if os.path.isfile(self.model.filePath(model_idxBelow)):
                                self.tree.setCurrentIndex(proxy_idxBelow)
                
                except Exception as e:
                    logger.error(f'File delete error: {e}')

    def onMenuRename(self):
        proxy_index = self.tree.currentIndex()
        if proxy_index.isValid():
            model_index = self.proxy.mapToSource(proxy_index)
            self.model.setReadOnly(False)
            self.tree.edit(proxy_index)

    def onFileRenamed(self, path, oldName, newName):
        self.model.setReadOnly(True)

    def onMenuInfo(self):
        strInfo = ""
        try:
            proxy_index = self.tree.currentIndex()
            if (proxy_index.isValid()):
                model_index = self.proxy.mapToSource(proxy_index)
                info = self.model.fileInfo(model_index)
                strInfo += f"Filename:  {info.fileName()}"
                strInfo += f"\nCreated:  {info.birthTime().toString()}"
                width = self.mw.glWidget.pixmap.width()
                height = self.mw.glWidget.pixmap.height()
                strInfo += f"\nImage Dims: {width} x {height}"           
            else:
                strInfo = "Invalid Index"
        except Exception as ex:
            strInfo = f'Unable to read picture file info: {ex}'

        #msgBox = QMessageBox(self)
        #msgBox.setWindowTitle("File Info")
        #msgBox.setText(strInfo)
        #msgBox.exec()
        self.dlgInfo.lblMessage.setText(strInfo)
        self.dlgInfo.exec()

    def hup(self):
        proxy_index = self.tree.currentIndex()
        if not proxy_index.isValid():
            return

        model_index = self.proxy.mapToSource(proxy_index)
        info = self.model.fileInfo(model_index)
        if not info.isFile():
            return

        if not self.mw.client:
            logger.error("HUP failed, client not initialized")
            return

        self.mw.client.transmit(bytearray(f"HUP\n\n{info.dir().dirName()}\r\n", 'utf-8'))
