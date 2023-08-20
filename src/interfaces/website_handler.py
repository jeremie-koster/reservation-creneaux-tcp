from src.domain.booking import BookingWish, BookingType
from src.interfaces.player_credentials import CredentialsFetcher
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup


def authenticate(driver, credentials: CredentialsFetcher, url: str):
    driver.get(url)

    user_field = driver.find_element(By.NAME, "info_text_login")
    user_field.clear()
    user_field.send_keys(credentials.login)

    password_field = driver.find_element(By.NAME, "info_text_password")
    password_field.clear()
    password_field.send_keys(credentials.password)

    password_field.send_keys(Keys.RETURN)

def complete_booking_form(driver, approximate_time_period: str, play_date: str, booking_type: BookingType):
    # besoin de two hour time period pour ideal time, booking type, date
    driver = complete_date(driver, play_date)
    driver = complete_time_period(driver, approximate_time_period)
    driver = complete_booking_type(driver, booking_type)

    validate_button = driver.find_element(By.XPATH,"//*[@id='boxModule']/form[2]/div/div/div[4]/button/span")
    validate_button.click()

    return driver

def complete_date(driver, play_date: str):
    date_input = driver.find_element(By.NAME, "affich_text_date")
    date_input.send_keys(play_date)
    return driver

def complete_time_period(driver, time_period: str):
    select = Select(driver.find_element(By.NAME, 'affich_select_horaire'))
    select.select_by_visible_text(time_period)
    return driver

def complete_booking_type(driver, booking_type: str):
    select = Select(driver.find_element(By.NAME, 'affich_select_reservationType'))
    select.select_by_visible_text(booking_type.value)
    return driver

def parse_slots_from_html(source_html: str):
    soup = BeautifulSoup(source_html, "html.parser")
    
    table = soup.find("table",attrs={"class":["liste"]})
    table_body = table.find("tbody")
    rows = table_body.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    
    return data