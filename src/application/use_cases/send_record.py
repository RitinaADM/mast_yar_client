from datetime import datetime
from src.domain.models import Record
from src.domain.ports.inbound.ui_port import UiPort
from src.domain.ports.outbound.http_port import HttpPort

class SendRecordUseCase:
    """Use case для отправки записи на сервер."""
    def __init__(self, http_port: HttpPort, ui_port: UiPort):
        self.http_port = http_port
        self.ui_port = ui_port

    def execute(self, click_counter: int) -> tuple[int, bool]:
        """Отправляет запись и возвращает обновленный счетчик кликов и success."""
        text = self.ui_port.get_text()
        if not text:
            self.ui_port.show_error("Текст не может быть пустым")
            return click_counter, False
        now = datetime.now()
        record = Record(
            text=text,
            date=now.strftime("%Y-%m-%d"),
            time=now.strftime("%H:%M:%S"),
            click_number=click_counter
        )
        try:
            self.http_port.send_post(record)
            return click_counter + 1, True
        except Exception as e:
            self.ui_port.show_error(str(e))
            return click_counter, False