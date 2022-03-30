from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Décoché")

        main_layout = QVBoxLayout(self)

        self.le_text = QLineEdit()
        self.lbl_text = QLabel("Veuillez taper du texte")
        self.btn_clear = QPushButton("Clear")

        main_layout.addWidget(self.le_text)
        main_layout.addWidget(self.lbl_text)
        main_layout.addWidget(self.btn_clear)

        self.le_text.textChanged.connect(self.lbl_text.setText)
        self.btn_clear.clicked.connect(self.clear_text)

    def clear_text(self):
        self.le_text.clear()
        self.lbl_text.setText("Veuillez taper du texte")


# Instantiation Qapplication affectée a la variable app
app = QApplication()
main_windows = MainWindow()
main_windows.show()
app.exec()
