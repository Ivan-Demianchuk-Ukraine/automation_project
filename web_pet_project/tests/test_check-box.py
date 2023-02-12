from web_pet_project.resources import *


@pytest.fixture()
def path_fixture():
    path = r'C:\Users\PREDATOR\PycharmProjects\pythonProject\automation_project\drivers\chromedriver'
    return path

@allure.step('Perform selecting check-box 1')
def test_check_box(path_fixture):
    driver = Chrome(service=Service(path_fixture))
    driver.get(base_url)
    checkboxes_link = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[6]/a')
    checkboxes_link.click()
    # time.sleep(2)
    first_box_locator = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
    first_box_locator.click()
    # time.sleep(2)
    driver.quit()


@allure.step('Perform unchecking box 2')
def test_uncheck_box(path_fixture):
    driver = Chrome(service=Service(path_fixture))
    driver.get(base_url)
    checkboxes_link = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[6]/a')
    checkboxes_link.click()
    # time.sleep(2)
    first_box_locator = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')
    first_box_locator.click()
    # time.sleep(2)
    driver.quit()
