from web_pet_project.helpers import *
from web_pet_project.all_locators import base_locator_instance


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('Custom_Epic')
@allure.feature('dropdown with countries')
@allure.step('Perform selecting drop-down option-1')
def test_dropdown_option_1():
    driver = Chrome(service=Service(path_to_driver))
    driver.get(base_url)
    base_locator_instance.dropdown_locator(driver).click()
    dropdown_locator = driver.find_element(By.ID, 'dropdown')
    dropdown_locator.click()
    option_1_locator = driver.find_element(By.XPATH, '//*[@id="dropdown"]/option[2]')
    option_1_locator.click()


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('Custom_Epic')
@allure.feature('dropdown with countries')
@allure.step('Perform selecting drop-down option-2')
def test_dropdown_option_2():
    driver = Chrome(service=Service(path_to_driver))
    driver.get(base_url)
    base_locator_instance.dropdown_locator(driver).click()
    dropdown_locator = driver.find_element(By.ID, 'dropdown')
    dropdown_locator.click()
    option_2_locator = driver.find_element(By.XPATH, '//*[@id="dropdown"]/option[3]')
    dropdown_locator.click()
    option_2_locator.click()
    driver.quit()
