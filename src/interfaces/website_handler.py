from src.interfaces.player_credentials import CredentialsFetcher
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def authenticate(driver, credentials: CredentialsFetcher, url: str):
    driver.get(url)

    user_field = driver.find_element(By.NAME, "info_text_login")
    user_field.clear()
    user_field.send_keys(credentials.login)

    password_field = driver.find_element(By.NAME, "info_text_password")
    password_field.clear()
    password_field.send_keys(credentials.password)

    password_field.send_keys(Keys.RETURN)

