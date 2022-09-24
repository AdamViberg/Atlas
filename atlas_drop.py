from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox
import sys
import pandas as pd

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atlas, Shehpherd of Atlantis")
        self.resize(720, 480)
        self.setAcceptDrops(True)

        self.label = QLabel()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            path = f
            df = pd.read_csv(path)
            df["Position"] = df["Position"] * 3
            df.to_csv(path,index=False)

            length = len(df)
            message = f"Succesfully transformed to {length} rows!"

            print("Success")

            msg = QMessageBox()
            msg.setWindowTitle(" ")
            msg.setText(message)
            msg.exec()

    
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWidget()
    ui.show()
    sys.exit(app.exec())