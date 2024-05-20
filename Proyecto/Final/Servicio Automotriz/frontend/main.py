from PySide2.QtWidgets import QMainWindow, QApplication, QDialog
from backend.mainwindow import MainWindow
from backend.loginwindow import LoginWindow
import sys


app = QApplication()

login_window = LoginWindow()
result = login_window.exec_()

if result == QDialog.Accepted:
    window = MainWindow()
    window.show()
    window.setWindowTitle("Servicio Automotriz")
    sys.exit(app.exec_())

else:
    sys.exit(0)
