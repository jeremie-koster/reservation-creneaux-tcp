import pandas as pd
from pandas.testing import assert_frame_equal
from src.repositories.transformations import create_df_from_parsing, clean_booking_slots

def test_create_df_from_parsing():
    input_slots = [['20:45\xa0-\xa021:30', '2', '1 GS W'], ['20:45\xa0-\xa021:30', '2', '12 GS ext W'], ['20:45\xa0-\xa021:30', '2', '13 GS W ext'], ['20:45\xa0-\xa021:30', '2', '16 TB W ext'], ['20:45\xa0-\xa021:30', '2', '3 GS W'], ['20:45\xa0-\xa021:30', '2', '4 GS W'], ['20:45\xa0-\xa021:30', '2', '5 GS W'], ['20:45\xa0-\xa021:30', '2', '6 GS W'], ['20:45\xa0-\xa021:30', '2', '7 TB W ext'], ['21:00\xa0-\xa021:45', '2', '2 GS W'], ['21:00\xa0-\xa021:45', '2', '8 TB W ext'], ['21:15\xa0-\xa022:00', '2', '15 TB W ext'], ['21:15\xa0-\xa022:00', '2', '9 TB W ext'], ['21:30\xa0-\xa022:15', '2', '1 GS W'], ['21:30\xa0-\xa022:15', '2', '12 GS ext W'], ['21:30\xa0-\xa022:15', '2', '13 GS W ext'], ['21:30\xa0-\xa022:15', '2', '16 TB W ext'], ['21:30\xa0-\xa022:15', '2', '3 GS W'], ['21:30\xa0-\xa022:15', '2', '4 GS W'], ['21:30\xa0-\xa022:15', '2', '5 GS W'], ['21:30\xa0-\xa022:15', '2', '6 GS W'], ['21:30\xa0-\xa022:15', '2', '7 TB W ext'], ['21:45\xa0-\xa022:30', '2', '2 GS W'], ['21:45\xa0-\xa022:30', '2', '8 TB W ext']]

    output_df = create_df_from_parsing(input_slots)

    expected_json_path = "test/unit/data/repositories/output/slots_df_expected.json"
    expected = pd.read_json(expected_json_path, dtype=False)
    
    assert_frame_equal(output_df, expected)
    
def test_clean_booking_slots():
    input_path = "test/unit/data/repositories/input/slots_df_before_cleaning.json"
    input_slots = pd.read_json(input_path)

    result = clean_booking_slots(input_slots)

    expected_path = "test/unit/data/repositories/output/slots_cleaned.json"
    expected = pd.read_json(expected_path, dtype=False)
    assert_frame_equal(result, expected)
    