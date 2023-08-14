"""
This class contains the booking business logic
"""

from dataclasses import dataclass
from datetime import date, datetime, time
from enum import Enum


class Surface(Enum):
    CLAY = "TB"
    HARD = "GS"


class Booking:
    pass


@dataclass
class Partner:
    first_name: str
    last_name: str


class BookingWish:
    def __init__(
        self,
        partner_first_name: str,
        partner_last_name: str,
        court_surface: Surface,
        date: str,
        min_start_time: str,
        max_start_time: str,
    ) -> None:
        self.partner = Partner(partner_first_name, partner_last_name)
        self.court_surface = court_surface
        self.date_of_play = self.set_date_of_play(date)
        self.min_start_time = self.set_time_of_play(min_start_time)
        self.max_start_time = self.set_time_of_play(max_start_time)

    def set_date_of_play(play_date: str) -> date:
        pass

    def set_time_of_play(play_time: str) -> time:
        pass
