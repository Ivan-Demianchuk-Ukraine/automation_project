from web_pet_project.helpers import *
from web_pet_project.all_locators import base_locator_instance, auth_instance
from web_pet_project.confest import driver


@allure.description('this test verifies that user can enter in the own account')
@allure.severity(allure.severity_level.BLOCKER)
@allure.epic('Custom_Epic')
@allure.feature('authorize of user')
@allure.step('Perform success login')
def test_login_success(driver):
    driver.get(base_url)
    base_locator_instance.auth_locator(driver).click()
    auth_instance.username_locator(driver).send_keys('tomsmith')
    auth_instance.password_locator(driver).send_keys('SuperSecretPassword!')
    auth_instance.submit_button(driver).click()
    driver.quit()


@allure.description('this test verifies that user cant enter in the own account without right credentials')
@allure.severity(allure.severity_level.BLOCKER)
@allure.epic('Custom_Epic')
@allure.feature('authorize of user')
@allure.step('Perform failed login')
def test_login_fail(driver):
    driver.get(base_url)
    base_locator_instance.auth_locator(driver).click()
    auth_instance.username_locator(driver).send_keys('invalid_username')
    auth_instance.password_locator(driver).send_keys('invalid_password')
    auth_instance.submit_button(driver).click()
    driver.quit()
