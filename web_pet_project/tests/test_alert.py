import allure


@allure.step('Perform canceling on alert')
def test_cancel_alert():
    import time
    # time.sleep(2)
    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    path = r'C:\Users\PREDATOR\PycharmProjects\pythonProject\automation_project\drivers\chromedriver'
    driver = Chrome(service=Service(path))
    driver.get('http://the-internet.herokuapp.com/')
    alert_link = driver.find_element(By.LINK_TEXT, 'JavaScript Alerts')
    alert_link.click()
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
    import time
    # time.sleep(2)
    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    path = r'C:\Users\PREDATOR\PycharmProjects\pythonProject\automation_project\drivers\chromedriver'
    driver = Chrome(service=Service(path))
    driver.get('http://the-internet.herokuapp.com/')
    alert_link = driver.find_element(By.LINK_TEXT, 'JavaScript Alerts')
    alert_link.click()
    # time.sleep(2)
    confirm_alert_locator = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
    confirm_alert_locator.click()
    # time.sleep(2)
    driver.switch_to.alert.accept()
    # time.sleep(2)
    driver.quit()
