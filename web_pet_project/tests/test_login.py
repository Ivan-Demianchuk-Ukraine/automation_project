from web_pet_project.helpers import *
from web_pet_project.all_locators import base_locator_instance


@allure.step('Perform success login')
def test_login_success():
    driver = Chrome(service=Service(path_to_driver))
    driver.get(base_url)
    base_locator_instance.auth_locator(driver).click()
    user_name_locator = driver.find_element(By.ID, 'username')
    user_name_locator.send_keys('tomsmith')
    password_locator = driver.find_element(By.ID, 'password')
    password_locator.send_keys('SuperSecretPassword!')
    submit_button = driver.find_element(By.XPATH, '//*[@id="login"]/button/i')
    submit_button.click()
    time.sleep(2)
    driver.quit()


@allure.step('Perform failed login')
def test_login_fail():
    driver = Chrome(service=Service(path_to_driver))
    driver.get(base_url)
    base_locator_instance.auth_locator(driver).click()
    user_name_locator = driver.find_element(By.ID, 'username')
    user_name_locator.send_keys('InvalidLogin')
    password_locator = driver.find_element(By.ID, 'password')
    password_locator.send_keys('InvalidPassword')
    submit_button = driver.find_element(By.XPATH, '//*[@id="login"]/button/i')
    submit_button.click()
    time.sleep(2)
    driver.quit()
