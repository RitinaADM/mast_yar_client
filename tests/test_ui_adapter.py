import pytest
from PySide6.QtCore import Qt
from src.infrastructure.adapters.inbound.ui_adapter import UiAdapter
from src.application.services import ClientService
from src.domain.ports.outbound.http_port import HttpPort
from src.domain.models import ResponseRecord

class MockHttpPort(HttpPort):
    def send_post(self, record):
        pass

    def get_records(self):
        return []

@pytest.fixture
def service():
    return ClientService(MockHttpPort(), None)

def test_ui_init(qtbot, service):
    ui = UiAdapter(service)
    qtbot.addWidget(ui)
    assert ui.line_edit is not None
    assert ui.list_view is not None
    assert ui.post_button.text() == "Отправить POST"

def test_get_text(qtbot, service):
    ui = UiAdapter(service)
    qtbot.addWidget(ui)
    ui.line_edit.setText("test")
    assert ui.get_text() == "test"

def test_display_records(qtbot, service):
    ui = UiAdapter(service)
    qtbot.addWidget(ui)
    records = [ResponseRecord(id=1, text="test", date="date", time="time", click_number=0)]
    ui.display_records(records)
    model = ui.list_view.model()
    assert model.rowCount() == 1

def test_post_click_success(qtbot, mocker):
    ui = UiAdapter(service=None)
    qtbot.addWidget(ui)
    service = ClientService(MockHttpPort(), ui)
    ui.service = service
    mocker.patch.object(service, 'send_record', return_value=(1, True))
    ui.line_edit.setText("test")
    qtbot.mouseClick(ui.post_button, Qt.MouseButton.LeftButton)
    assert ui.line_edit.text() == ""  # Проверяем, что поле очистилось