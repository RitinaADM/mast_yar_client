from typing import List
from PySide6.QtCore import Qt
from src.infrastructure.adapters.inbound.ui_adapter import UiAdapter
from src.application.services import ClientService
from src.domain.ports.outbound.http_port import HttpPort
from src.domain.models import Record, ResponseRecord

class MockHttpPort(HttpPort):
    def send_post(self, record: Record) -> None:
        pass

    def get_records(self) -> List[ResponseRecord]:
        return [ResponseRecord(id=1, text="test", date="2025-08-20", time="12:00:00", click_number=0)]

def test_ui_to_service_integration(qtbot, mocker):
    http_port = MockHttpPort()
    ui = UiAdapter(service=None)
    qtbot.addWidget(ui)
    service = ClientService(http_port, ui)
    ui.service = service
    mocker.patch.object(http_port, 'send_post')
    ui.line_edit.setText("test")
    qtbot.mouseClick(ui.post_button, Qt.MouseButton.LeftButton)
    assert ui.line_edit.text() == ""  # Проверяем, что поле очистилось
    http_port.send_post.assert_called_once()