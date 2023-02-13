from web_pet_project.helpers import *
from web_pet_project.all_locators import base_locator_instance, checkbox_instance
from web_pet_project.confest import driver


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic('Custom_Epic')
@allure.feature('check-box functionality')
@allure.step('Perform selecting check-box 1')
def test_check_box(driver):
    driver.get(base_url)
    base_locator_instance.checkbox_locator(driver).click()
    checkbox_instance.checkbox_option_1(driver).click()
    time.sleep(2)
    driver.quit()


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic('Custom_Epic')
@allure.feature('check-box functionality')
@allure.step('Perform unchecking box 2')
def test_uncheck_box(driver):
    driver.get(base_url)
    base_locator_instance.checkbox_locator(driver).click()
    checkbox_instance.checkbox_option_2(driver).click()
    time.sleep(2)
    driver.quit()
