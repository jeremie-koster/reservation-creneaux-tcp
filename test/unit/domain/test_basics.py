from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_website_connection(browser):
    url = "https://www.tennisclubdeparis.fr/"
    browser.get(url)
    print("Test")
    assert "TCP - Accueil" in browser.title

