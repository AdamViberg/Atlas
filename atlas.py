from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Atlas, shepherd of Atlantis")

        self.label = QLabel()
        self.btn = QPushButton("Press me!")
        self.input = QLineEdit()


        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        layout.addWidget(self.btn)
        self.btn.clicked.connect(self.click_btn)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def click_btn(self):
        name = self.input.text()
        self.label.setText(name)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()