from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from db_response import DbResponse


class IDatabase(ABC):

    def __init__(self, db_name: str):
        self.db_name = db_name
    @abstractmethod
    def connect(self) -> DbResponse:
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute(self, query: str, params: list = None) -> DbResponse:
        pass

    @abstractmethod
    def fetch_all(self) -> DbResponse:
        pass

    @abstractmethod
    def fetch_one(self) -> DbResponse:
        pass

    @abstractmethod
    def fetch_many(self, size: int) -> DbResponse:
        pass

    @abstractmethod
    def insert(self, data: dict) -> DbResponse:
        pass

    @abstractmethod
    def insert_many(self, data: list) -> DbResponse:
        pass

    @abstractmethod
    def update(self, data: dict) -> DbResponse:
        pass

    @abstractmethod
    def delete(self, data: dict) -> DbResponse:
        pass

