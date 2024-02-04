
from typing import Any

from db_const import DbResponseCode


class DbResponse:
    def __init__(self):
        self.message = None
        self.data = None
        self.status: DbResponseCode = DbResponseCode.UNKNOWN

    def get_data(self) -> Any:
        return self.data

    def set_data(self, data: Any):
        self.data = data

    def get_status(self) -> DbResponseCode:
        return self.status


    def set_status(self, status: DbResponseCode):
        self.status = status


    def get_message(self) -> str:
        return self.message


    def set_message(self, message: str):
        self.message = message