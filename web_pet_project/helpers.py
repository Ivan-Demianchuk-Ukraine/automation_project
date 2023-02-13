import sys
import json
sys.path.append(r'C:\Users\PREDATOR\PycharmProjects\pythonProject\automation_project\web_pet_project\config.json')
import allure
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest


with open(r'C:\Users\PREDATOR\PycharmProjects\pythonProject\automation_project\web_pet_project\config.json') as f:
    config = json.load(f)
base_url = config['base_url']

path_to_driver = r'C:\Users\PREDATOR\PycharmProjects\pythonProject\automation_project\drivers\chromedriver'


class TestException:
    pass
