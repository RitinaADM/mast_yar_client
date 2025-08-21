from abc import ABC, abstractmethod
from typing import List
from src.domain.models import ResponseRecord

class UiPort(ABC):
    @abstractmethod
    def get_text(self) -> str:
        pass

    @abstractmethod
    def display_records(self, records: List[ResponseRecord]) -> None:
        pass

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def show_error(self, message: str) -> None:
        pass