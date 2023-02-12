from web_pet_project.helpers import *


@allure.step('Perform selecting drop-down option-1')
def test_dropdown_option_1():
    driver = Chrome(service=Service(path_to_driver))
    driver.get(base_url)
    dropdown_link = driver.find_element(By.LINK_TEXT, 'Dropdown')
    dropdown_link.click()
    dropdown_locator = driver.find_element(By.ID, 'dropdown')
    dropdown_locator.click()
    # time.sleep(2)
    option_1_locator = driver.find_element(By.XPATH, '//*[@id="dropdown"]/option[2]')
    option_1_locator.click()
    # time.sleep(2)


@allure.step('Perform selecting drop-down option-2')
def test_dropdown_option_2():
    driver = Chrome(service=Service(path_to_driver))
    driver.get(base_url)
    dropdown_link = driver.find_element(By.LINK_TEXT, 'Dropdown')
    dropdown_link.click()
    dropdown_locator = driver.find_element(By.ID, 'dropdown')
    dropdown_locator.click()
    # time.sleep(2)
    option_2_locator = driver.find_element(By.XPATH, '//*[@id="dropdown"]/option[3]')
    dropdown_locator.click()
    # time.sleep(2)
    option_2_locator.click()
    # time.sleep(2)
    driver.quit()
