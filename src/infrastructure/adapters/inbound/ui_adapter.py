from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QListView, QPushButton, QMessageBox
from PySide6.QtCore import QStringListModel
from typing import List, Optional
from src.domain.models import ResponseRecord
from src.domain.exceptions import ClientError
from src.application.services import ClientService

# Настройка логирования с ротацией
import logging.handlers
handler = logging.handlers.RotatingFileHandler('app.log', maxBytes=1000000, backupCount=5)
logging.basicConfig(level=logging.INFO, handlers=[handler])
logger = logging.getLogger(__name__)

class UiAdapter(QWidget):
    """Адаптер для UI на основе PySide6."""
    def __init__(self, service: Optional[ClientService] = None):
        super().__init__()
        self.service = service
        self.init_ui()

    def init_ui(self):
        """Инициализирует элементы интерфейса."""
        layout = QVBoxLayout()
        self.line_edit = QLineEdit(self)
        self.list_view = QListView(self)
        self.post_button = QPushButton("Отправить POST", self)
        self.get_button = QPushButton("Получить записи", self)

        self.post_button.clicked.connect(self.on_post_click)
        self.get_button.clicked.connect(self.on_get_click)

        layout.addWidget(self.line_edit)
        layout.addWidget(self.list_view)
        layout.addWidget(self.post_button)
        layout.addWidget(self.get_button)
        self.setLayout(layout)

    def on_post_click(self):
        """Обработчик клика по кнопке POST."""
        if self.service is None:
            logger.error("Service not initialized")
            self.show_error("Сервис не инициализирован")
            return
        self.click_counter, success = self.service.send_record()
        if success:
            self.line_edit.clear()
            logger.info("Record sent successfully")

    def on_get_click(self):
        """Обработчик клика по кнопке GET."""
        if self.service is None:
            logger.error("Service not initialized")
            self.show_error("Сервис не инициализирован")
            return
        try:
            self.service.fetch_and_display()
        except ClientError as e:
            logger.error(f"Ошибка при получении записей: {e}")
            self.show_error(str(e))

    def get_text(self) -> str:
        """Получает текст из QLineEdit."""
        return self.line_edit.text()

    def display_records(self, records: List[ResponseRecord]):
        """Отображает записи в QListView."""
        model = QStringListModel()
        model.setStringList([f"{r.id}: {r.text} ({r.date} {r.time}, клик {r.click_number})" for r in records])
        self.list_view.setModel(model)

    def run(self):
        """Запускает UI."""
        self.show()

    def show_error(self, message: str):
        QMessageBox.critical(self, "Ошибка", message)