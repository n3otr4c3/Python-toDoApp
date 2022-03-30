from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from functools import partial


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QHBoxLayout(self)

        self.btn_left = QPushButton("Left")
        self.btn_right = QPushButton("Right")

        main_layout.addWidget(self.btn_left)
        main_layout.addWidget(self.btn_right)

        self.btn_left.clicked.connect(partial(self.button_clicked, "Bouton de gauche"))
        self.btn_right.clicked.connect(partial(self.button_clicked, "Bouton de droite"))

    def button_clicked(self, message):
        print(message)


# Instantiation Qapplication affectée a la variable app
app = QApplication()
main_windows = MainWindow()
main_windows.show()
app.exec()
