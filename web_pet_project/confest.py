from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def driver():
    path_to_driver = r'C:\Users\PREDATOR\PycharmProjects\pythonProject\automation_project\drivers\chromedriver'
    driver = Chrome(service=Service(path_to_driver))
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
