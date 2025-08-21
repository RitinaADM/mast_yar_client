import requests
from typing import List
from src.domain.models import Record, ResponseRecord
from src.domain.ports.outbound.http_port import HttpPort
from src.domain.exceptions import HttpRequestError

class HttpAdapter(HttpPort):
    def __init__(self, post_url: str, get_url: str):
        self.post_url = post_url
        self.get_url = get_url

    def send_post(self, record: Record) -> None:
        try:
            response = requests.post(self.post_url, json=record.model_dump(), timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            raise HttpRequestError(f"Failed to send POST request: {e}")

    def get_records(self) -> List[ResponseRecord]:
        try:
            response = requests.get(self.get_url, timeout=5)
            response.raise_for_status()
            data = response.json()
            if not isinstance(data, dict) or "records" not in data:
                raise HttpRequestError("Ожидался словарь с 'records'")
            records_data = data["records"]
            if not isinstance(records_data, list):
                raise HttpRequestError("Ожидался список записей")
            return [ResponseRecord(**item) for item in records_data]
        except requests.RequestException as e:
            raise HttpRequestError(f"Failed to fetch records: {e}")