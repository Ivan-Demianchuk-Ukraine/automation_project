from web_pet_project.helpers import *
from web_pet_project.all_locators import base_locator_instance, auth_instance
from web_pet_project.confest import driver


@allure.description('this test verifies that user can enter in the own account')
@allure.severity(allure.severity_level.BLOCKER)
@allure.epic('Custom_Epic')
@allure.feature('authorize of user')
@allure.step('Perform success login')
def test_login_success(driver):
    """
    1. Navigate to base url
    2. Enter 'tomsmith'
    3. Enter 'SuperSecretPassword!' as password
    4. Click 'Login' button
    Verify that the 'You logged into a secure area!' text is displayed and there is 'Logout' button.
    """
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
    """
    1. Navigate to base url
    2. Enter the 'invalid_username' value
    3. Enter the 'invalid_password' value
    4. Click 'Login' button
    Verify that the 'You logged into a secure area!' is not displayed.
    Verify that 'Logout' button is absent.
    Verify that there is 'Login' button.
    Verify that 'Your username is invalid' text is displayed.
    """
    driver.get(base_url)
    base_locator_instance.auth_locator(driver).click()
    auth_instance.username_locator(driver).send_keys('invalid_username')
    auth_instance.password_locator(driver).send_keys('invalid_password')
    auth_instance.submit_button(driver).click()
    time.sleep(10)
    driver.quit()
