from src.domain.ports.inbound.ui_port import UiPort
from src.domain.ports.outbound.http_port import HttpPort

class FetchRecordsUseCase:
    """Use case для получения и отображения записей."""
    def __init__(self, http_port: HttpPort, ui_port: UiPort):
        self.http_port = http_port
        self.ui_port = ui_port

    def execute(self) -> None:
        """Получает записи и отображает их в UI."""
        records = self.http_port.get_records()
        self.ui_port.display_records(records)