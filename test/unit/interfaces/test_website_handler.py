import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.interfaces.player_credentials import LocalCredentialsFetcher
from src.interfaces.website_handler import authenticate
from src.usecases.uc_booking import TCP_WEBSITE_URL


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
