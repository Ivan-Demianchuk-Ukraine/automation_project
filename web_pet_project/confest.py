from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import sys
import os


import pytest


@pytest.fixture()
def driver():
    path_to_driver = os.path.join(os.path.dirname(sys.path[0]), 'automation_project/web_pet_project/chromedriver')
    driver = Chrome(service=Service(path_to_driver))
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
