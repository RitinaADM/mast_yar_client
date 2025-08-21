from src.domain.ports.inbound.ui_port import UiPort
from src.domain.ports.outbound.http_port import HttpPort
from src.application.use_cases.send_record import SendRecordUseCase
from src.application.use_cases.fetch_records import FetchRecordsUseCase

class ClientService:
    """Сервис для координации use cases клиента."""
    def __init__(self, http_port: HttpPort, ui_port: UiPort):
        self.http_port = http_port
        self.ui_port = ui_port
        self.click_counter = 0
        self.send_use_case = SendRecordUseCase(http_port, ui_port)
        self.fetch_use_case = FetchRecordsUseCase(http_port, ui_port)

    def send_record(self) -> tuple[int, bool]:
        """Координирует отправку записи."""
        self.click_counter, success = self.send_use_case.execute(self.click_counter)
        return self.click_counter, success

    def fetch_and_display(self) -> None:
        """Координирует получение и отображение записей."""
        self.fetch_use_case.execute()