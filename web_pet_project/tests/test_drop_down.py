from web_pet_project.helpers import *
from web_pet_project.all_locators import base_locator_instance, dropdown_instance
from web_pet_project.confest import driver


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('Custom_Epic')
@allure.feature('dropdown with countries')
@allure.step('Perform selecting drop-down option-1')
def test_dropdown_option_1(driver):
    driver.get(base_url)
    base_locator_instance.dropdown_locator(driver).click()
    dropdown_instance.dropdown(driver).click()
    dropdown_instance.dropdown_option_1(driver).click()


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('Custom_Epic')
@allure.feature('dropdown with countries')
@allure.step('Perform selecting drop-down option-2')
def test_dropdown_option_2(driver):
    driver.get(base_url)
    base_locator_instance.dropdown_locator(driver).click()
    dropdown_instance.dropdown(driver).click()
    dropdown_instance.dropdown_option_2(driver).click()
    driver.quit()
