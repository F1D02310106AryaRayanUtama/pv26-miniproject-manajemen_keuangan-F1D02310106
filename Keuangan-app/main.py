import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from database.db import create_table

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("styles/style.qss", "r") as f:
        app.setStyleSheet(f.read())

    # buat tabel saat pertama kali run
    create_table()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())