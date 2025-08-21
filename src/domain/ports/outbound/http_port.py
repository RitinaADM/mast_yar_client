from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Record, ResponseRecord

class HttpPort(ABC):
    @abstractmethod
    def send_post(self, record: Record) -> None:
        pass

    @abstractmethod
    def get_records(self) -> List[ResponseRecord]:
        pass