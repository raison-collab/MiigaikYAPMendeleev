import typing

from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit

from CSVManager import CSVManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('main_window.ui', self)

        self.label: QLabel = self.findChild(QLabel, 'label')

        self.pixmap: typing.Optional[QPixmap] = None

        self.set_image('Periodic_table_ru.svg.png')
        self.resize(self.pixmap.width(), self.height())

        self.input: QLineEdit = self.findChild(QLineEdit, 'lineEdit')

        self.text_edit: QTextEdit = self.findChild(QTextEdit, 'textEdit')

        self.button: QPushButton = self.findChild(QPushButton, 'pushButton')

        self.csv_manager = CSVManager()

        self.set_events()

    def set_image(self, image_path: str):
        self.pixmap = QPixmap(image_path)
        self.label.setPixmap(self.pixmap)

    def set_events(self):
        self.button.clicked.connect(self.show_element_data)

    def validation_input_number(self):
        if not self.input.text().isdigit() or int(self.input.text()) < 1 or int(self.input.text()) > len(self.csv_manager.read_file()):
            return False
        return True

    def show_element_data(self):
        if not self.validation_input_number():
            self.text_edit.setText('Ошибка')
            return

        self.text_edit.setText(self.csv_manager.get_data_by_id(int(self.input.text())))

