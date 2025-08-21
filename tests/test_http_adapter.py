import pytest
import requests
from src.infrastructure.adapters.outbound.http_adapter import HttpAdapter
from src.domain.exceptions import HttpRequestError
from src.domain.models import Record, ResponseRecord

@pytest.fixture
def adapter():
    return HttpAdapter("http://test/post", "http://test/get")

def test_send_post(mocker, adapter: HttpAdapter):
    mock_post = mocker.patch.object(requests, 'post')
    record = Record(text="test", date="date", time="time", click_number=0)
    adapter.send_post(record)
    mock_post.assert_called_once_with("http://test/post", json=record.model_dump(), timeout=5)

def test_get_records(mocker, adapter: HttpAdapter):
    mock_get = mocker.patch.object(requests, 'get')
    mock_get.return_value.json.return_value = {"records": [{"id": 1, "text": "test", "date": "date", "time": "time", "click_number": 0}]}
    records = adapter.get_records()
    assert len(records) == 1
    assert isinstance(records[0], ResponseRecord)
    assert records[0].id == 1

def test_http_error(mocker, adapter: HttpAdapter):
    mock_post = mocker.patch.object(requests, 'post')
    mock_post.return_value.raise_for_status.side_effect = requests.RequestException("Network error")
    with pytest.raises(HttpRequestError, match="Failed to send POST request: Network error"):
        adapter.send_post(Record(text="test", date="date", time="time", click_number=0))