"""
This class contains the booking business logic
"""

from dataclasses import dataclass
from datetime import date, time
from enum import Enum
from typing import Union


class Surface(Enum):
    CLAY = "TB"
    HARD = "GS"

class BookingType(Enum):
    SINGLE = "Single web"
    DOUBLE = "Double web"
    PADEL_SINGLE = "Padel - Simple web"
    PADEL_DOUBLE = "Padel - Double web"
    PRIORITY = "Prioritaire web"

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
        date: str,
        ideal_start_time: str,
        court_surface: Surface = None,
        min_start_time: str = None,
        max_start_time: str = None,
    ) -> None:
        """Class representing the booking request.

        Args:
            partner_first_name (str): First name of the player the user wants to play with
            partner_last_name (str): Last name of the player the user wants to play with
            date (str): The date the user wants to play. Expected format is dd/mm/yyyy.
            ideal_start_time (str): The ideal start time of the tennis session. Expected format is HH:MM.
            court_surface (Surface, optional): Court surface wanted. Defaults to None.
            min_start_time (str, optional): Minimum start time of the session (the session shouldn't begin before that time). Defaults to None.
            max_start_time (str, optional): Maximum start time of the session (the session shouldn't begin after that time). Defaults to None.
        """
        self.partner = Partner(partner_first_name, partner_last_name)
        self.court_surface = court_surface
        self.date_of_play = self.set_date_of_play(date)
        self.ideal_start_time = self.set_time_of_play(ideal_start_time)
        self.min_start_time = self.set_time_of_play(min_start_time)
        self.max_start_time = self.set_time_of_play(max_start_time)

    # TODO - ça dépendra du format envoyé par discord
    def set_date_of_play(self, play_date: str) -> date:
        return play_date

    # TODO - ça dépendra du format envoyé par discord
    def set_time_of_play(self, play_time: str) -> time:
        if play_time:
            hour, minutes = play_time.split(":")
            return time(int(hour), int(minutes))

    @staticmethod
    def get_time_period_starting_at(play_time: Union[time, str]) -> str:
        if isinstance(play_time, time):
            hour = play_time.hour
        elif isinstance(play_time, str):
            hour = int(play_time.split(":")[0])
        hour_plus_two = hour + 2
        hour, hour_plus_two = [f"0{hour_digit}" if hour_digit < 10 else hour_digit for hour_digit in [hour, hour_plus_two]]
        return f"{hour}:00 / {hour_plus_two}:00"
