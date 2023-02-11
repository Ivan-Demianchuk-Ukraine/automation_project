import allure


@allure.step('Perform success login')
def test_login_success():
    import time
    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from web_pet_project.tests.resources import base_url
    path = r'C:\Users\PREDATOR\PycharmProjects\pythonProject\automation_project\drivers\chromedriver'
    driver = Chrome(service=Service(path))
    driver.get(base_url)
    auth_link = driver.find_element(By.LINK_TEXT, 'Form Authentication')
    auth_link.click()
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
    import time
    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    import web_pet_project.tests.resources as res
    path = r'C:\Users\PREDATOR\PycharmProjects\pythonProject\automation_project\drivers\chromedriver'
    driver = Chrome(service=Service(path))
    driver.get(res.base_url)
    auth_link = driver.find_element(By.LINK_TEXT, 'Form Authentication')
    auth_link.click()
    user_name_locator = driver.find_element(By.ID, 'username')
    user_name_locator.send_keys('InvalidLogin')
    password_locator = driver.find_element(By.ID, 'password')
    password_locator.send_keys('InvalidPassword')
    submit_button = driver.find_element(By.XPATH, '//*[@id="login"]/button/i')
    submit_button.click()
    time.sleep(2)
    driver.quit()
