from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QLineEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ToDo++")
        self.setMinimumSize(400, 500)
        self.setWindowIcon(QtGui.QIcon('res/icon.png'))

        main_layout = QVBoxLayout(self)

        self.list = QListWidget()
        self.textBox = QLineEdit()
        self.textBox.setPlaceholderText("Ajouter une nouvelle tâche...")
        self.btn_clear = QPushButton("Tout supprimer")

        main_layout.addWidget(self.list)
        main_layout.addWidget(self.textBox)
        main_layout.addWidget(self.btn_clear)

        self.textBox.returnPressed.connect(self.insert_text)
        self.btn_clear.clicked.connect(self.clear_text)
        self.list.itemDoubleClicked.connect(self.clear_task)

    def clear_task(self, item):
        self.list.takeItem(self.list.row(item))

    def insert_text(self):
        # text = self.textBox.text()
        # self.list.addItem(text)
        self.list.addItem(self.textBox.text())
        self.textBox.clear()

    def clear_text(self):
        self.list.clear()


# Instantiation Qapplication affectée a la variable app
app = QApplication()
main_windows = MainWindow()
main_windows.show()
app.exec()
