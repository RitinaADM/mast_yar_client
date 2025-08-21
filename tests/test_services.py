import pytest
from src.application.services import ClientService
from src.domain.exceptions import HttpRequestError
from src.domain.ports.inbound.ui_port import UiPort
from src.domain.ports.outbound.http_port import HttpPort
from src.domain.models import Record, ResponseRecord
from typing import List

class MockHttpPort(HttpPort):
    def send_post(self, record: Record) -> None:
        pass

    def get_records(self) -> List[ResponseRecord]:
        return [ResponseRecord(id=1, text="test", date="2025-08-20", time="12:00:00", click_number=0)]

class MockUiPort(UiPort):
    def get_text(self) -> str:
        return "test"

    def display_records(self, records: List[ResponseRecord]) -> None:
        pass

    def run(self) -> None:
        pass

    def show_error(self, message: str) -> None:
        pass

@pytest.fixture
def service():
    return ClientService(MockHttpPort(), MockUiPort())

def test_send_record_success(service: ClientService):
    counter, success = service.send_record()
    assert success is True
    assert counter == 1

def test_fetch_and_display(service: ClientService):
    service.fetch_and_display()  # No exception means pass

def test_empty_text_error(service: ClientService):
    service.ui_port.get_text = lambda: ""
    counter, success = service.send_record()
    assert success is False
    assert counter == 0

def test_empty_records(service: ClientService):
    service.http_port.get_records = lambda: []
    service.fetch_and_display()  # Should handle empty list

def test_http_error_handling(mocker, service: ClientService):
    mocker.patch.object(service.http_port, 'send_post', side_effect=HttpRequestError("Network error"))
    counter, success = service.send_record()
    assert success is False
    assert counter == 0