import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'automation_project/web_pet_project/config.json'))
import allure
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest


with open(os.path.join(os.path.dirname(sys.path[0]), 'automation_project/web_pet_project/config.json')) as f:
    config = json.load(f)
base_url = config['base_url']


class TestException:
    pass
