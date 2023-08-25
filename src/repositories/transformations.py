from typing import List
import re

import pandas as pd


def create_df_from_parsing(booking_slots: List) -> pd.DataFrame:
    columns = ["time_period", "players_number", "court"]
    slots_df = pd.DataFrame(data=booking_slots, columns=columns)
    slots_df["slot_number"] = range(1, len(slots_df)+1)
    return slots_df

def clean_booking_slots(slots: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = slots.replace("\u00a0","")
    cleaned_df["time_period"] = cleaned_df["time_period"].str.split().str.join(" ")
    return cleaned_df

def format_slots_data(slots: pd.DataFrame) -> pd.DataFrame:
    slots['start_time'] = pd.to_datetime(slots['time_period'].str.split(' - ').str[0], format='%H:%M')
    slots["court_surface"] = slots["court"].str.extract(r"(\d+) (\w\w)", expand=False)[1]
    return slots