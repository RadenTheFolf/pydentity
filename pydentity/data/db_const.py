from enum import Enum


class DbResponseCode(Enum):
    UNKNOWN = None
    OK = 0
    ERROR = 1
    NOT_FOUND = 2
    DUPLICATE = 3
    INVALID = 4
    UNAUTHORIZED = 5
    FORBIDDEN = 6
    NOT_IMPLEMENTED = 7
    NOT_ALLOWED = 8
    BAD_REQUEST = 9
