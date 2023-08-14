from enum import Enum


class Usecase(Enum):
    BOOKING = "booking"
    UPDATE = "update"
    CANCEL = "cancel"
    FETCH_WISHES = "fetch_wishes"