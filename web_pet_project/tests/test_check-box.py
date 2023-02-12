from web_pet_project.helpers import *
from web_pet_project.all_locators import base_locator_instance



@allure.step('Perform selecting check-box 1')
def test_check_box():
    driver = Chrome(service=Service(path_to_driver))
    driver.get(base_url)
    base_locator_instance.checkbox_locator(driver).click()
    # time.sleep(2)
    first_box_locator = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
    first_box_locator.click()
    # time.sleep(2)
    driver.quit()


@allure.step('Perform unchecking box 2')
def test_uncheck_box():
    driver = Chrome(service=Service(path_to_driver))
    driver.get(base_url)
    base_locator_instance.checkbox_locator(driver).click()
    # time.sleep(2)
    first_box_locator = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')
    first_box_locator.click()
    # time.sleep(2)
    driver.quit()