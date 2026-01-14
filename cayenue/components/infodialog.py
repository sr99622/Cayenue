#*******************************************************************************
# Cayenue/cayenue/components/infodialog.py
#
# Copyright (c) 2026 Stephen Rhodes 
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
#******************************************************************************/
from PyQt6.QtWidgets import QGridLayout, QLabel, \
    QDialog, QPushButton
from PyQt6.QtCore import Qt

class InfoDialog(QDialog):
    def __init__(self, p):
        super().__init__(p)
        self.setWindowTitle("info")
        self.lblMessage = QLabel()
        self.btnOK = QPushButton("OK")
        self.btnOK.clicked.connect(self.hide)
        lytMain = QGridLayout(self)
        lytMain.addWidget(self.lblMessage, 0, 0, 1, 1)
        lytMain.addWidget(QLabel(),        1, 0, 1, 1)
        lytMain.addWidget(self.btnOK,      2, 0, 1, 1, Qt.AlignmentFlag.AlignCenter)
