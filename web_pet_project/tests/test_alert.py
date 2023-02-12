from web_pet_project.helpers import *
from web_pet_project.all_locators import base_locator_instance, alert_instance


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic('Custom_Epic')
@allure.feature('alert functionality')
@allure.step('Perform canceling on alert')
def test_cancel_alert():
    driver = Chrome(service=Service(path_to_driver))
    driver.get(base_url)
    base_locator_instance.alert_locator(driver).click()
    # time.sleep(2)
    alert_instance.confirm_alert_link_locator(driver).click()
    # time.sleep(2)
    driver.switch_to.alert.dismiss()
    # time.sleep(2)
    driver.quit()


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic('Custom_Epic')
@allure.feature('alert functionality')
@allure.step('Perform accepting on alert')
def test_accept_alert():
    driver = Chrome(service=Service(path_to_driver))
    driver.get(base_url)
    base_locator_instance.alert_locator(driver).click()
    # time.sleep(2)
    alert_instance.confirm_alert_link_locator(driver).click()
    # time.sleep(2)
    driver.switch_to.alert.accept()
    # time.sleep(2)
    driver.quit()