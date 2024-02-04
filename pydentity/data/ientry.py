from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class IEntry:
    id: str = None
    created_at: str = None
    updated_at: str = None

    @abstractmethod
    def set_id(self, id: str):
        pass

    @abstractmethod
    def get_id(self) -> str:
        pass

    @abstractmethod
    def set_created_at(self, created_at: str):
        pass

    @abstractmethod
    def get_created_at(self) -> str:
        pass

    @abstractmethod
    def set_updated_at(self, updated_at: str):
        pass

    @abstractmethod
    def get_updated_at(self) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @abstractmethod
    def from_dict(self, data: dict):
        pass