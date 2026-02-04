from PyQt6.QtCore import QSortFilterProxyModel

class FileSortProxy(QSortFilterProxyModel):
    def lessThan(self, left, right):
        model = self.sourceModel()

        left_info = model.fileInfo(left)
        right_info = model.fileInfo(right)

        if left_info.isDir() and not right_info.isDir():
            return True
        if not left_info.isDir() and right_info.isDir():
            return False

        if left_info.isDir() and right_info.isDir():
            return left_info.fileName().lower() < right_info.fileName().lower()

        return left_info.fileName().lower() > right_info.fileName().lower()

