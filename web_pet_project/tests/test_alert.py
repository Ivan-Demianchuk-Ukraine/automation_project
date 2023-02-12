from web_pet_project.helpers import *
from web_pet_project.all_locators import base_locator_instance


@allure.step('Perform canceling on alert')
def test_cancel_alert():
    driver = Chrome(service=Service(path_to_driver))
    driver.get(base_url)
    base_locator_instance.alert_locator(driver).click()
    # time.sleep(2)
    confirm_alert_locator = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
    confirm_alert_locator.click()
    # time.sleep(2)
    driver.switch_to.alert.dismiss()
    # time.sleep(2)
    confirm_alert_locator.click()
    # time.sleep(2)
    driver.switch_to.alert.accept()
    # time.sleep(2)
    driver.quit()


@allure.step('Perform accepting on alert')
def test_accept_alert():
    driver = Chrome(service=Service(path_to_driver))
    driver.get(base_url)
    base_locator_instance.alert_locator(driver).click()
    # time.sleep(2)
    confirm_alert_locator = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
    confirm_alert_locator.click()
    # time.sleep(2)
    driver.switch_to.alert.accept()
    # time.sleep(2)
    driver.quit()