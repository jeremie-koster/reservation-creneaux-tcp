from unittest.mock import Mock
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.interfaces.player_credentials import LocalCredentialsFetcher
from src.interfaces.website_handler import authenticate, parse_slots_from_html
from src.usecases.uc_booking import TCP_WEBSITE_URL
import os

@pytest.fixture
def setup_driver():
    return webdriver.Chrome()


def test_authenticate(setup_driver):
    # Given
    driver = setup_driver
    credentials_handler = LocalCredentialsFetcher()

    # When
    authenticate(driver, credentials_handler, TCP_WEBSITE_URL)

    # Then
    membership_element = driver.find_element(By.XPATH, "//*[@id='boxModule']/div/div[1]/div[2]/div[2]/div[2]/span")
    assert membership_element.text == "Membre depuis le"

def test_parse_slots_from_html():
    # print(os.listdir)
    input_html_path = "test/unit/data/interfaces/input/booking-slots.html"
    with open(input_html_path, "r") as input_html:
        html_content = input_html.read()

    output = parse_slots_from_html(html_content)

    expected = [['20:45\xa0-\xa021:30', '2', '1 GS W'], ['20:45\xa0-\xa021:30', '2', '12 GS ext W'], ['20:45\xa0-\xa021:30', '2', '13 GS W ext'], ['20:45\xa0-\xa021:30', '2', '16 TB W ext'], ['20:45\xa0-\xa021:30', '2', '3 GS W'], ['20:45\xa0-\xa021:30', '2', '4 GS W'], ['20:45\xa0-\xa021:30', '2', '5 GS W'], ['20:45\xa0-\xa021:30', '2', '6 GS W'], ['20:45\xa0-\xa021:30', '2', '7 TB W ext'], ['21:00\xa0-\xa021:45', '2', '2 GS W'], ['21:00\xa0-\xa021:45', '2', '8 TB W ext'], ['21:15\xa0-\xa022:00', '2', '15 TB W ext'], ['21:15\xa0-\xa022:00', '2', '9 TB W ext'], ['21:30\xa0-\xa022:15', '2', '1 GS W'], ['21:30\xa0-\xa022:15', '2', '12 GS ext W'], ['21:30\xa0-\xa022:15', '2', '13 GS W ext'], ['21:30\xa0-\xa022:15', '2', '16 TB W ext'], ['21:30\xa0-\xa022:15', '2', '3 GS W'], ['21:30\xa0-\xa022:15', '2', '4 GS W'], ['21:30\xa0-\xa022:15', '2', '5 GS W'], ['21:30\xa0-\xa022:15', '2', '6 GS W'], ['21:30\xa0-\xa022:15', '2', '7 TB W ext'], ['21:45\xa0-\xa022:30', '2', '2 GS W'], ['21:45\xa0-\xa022:30', '2', '8 TB W ext']]

    assert output == expected