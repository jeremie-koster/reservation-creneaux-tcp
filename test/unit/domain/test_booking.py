from datetime import time
from unittest.mock import patch
import pytest

from src.domain.booking import BookingWish


@pytest.mark.parametrize(
        "input, expected",
        [
            ("19:15", "19:00 / 21:00"),
            ("11:04", "11:00 / 13:00"),
            ("09:25", "09:00 / 11:00"),
            (time(7, 41), "07:00 / 09:00")
        ]
)
def test_get_time_period_starting_at(input, expected):
    booking = BookingWish("Val", "Mey", "25/12/2006", "14:10")
    
    result = booking.get_time_period_starting_at(input)

    assert result == expected
