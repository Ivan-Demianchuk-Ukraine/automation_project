from web_pet_project.helpers import *


class BasePage:

    @staticmethod
    def auth_locator(driver):
        return driver.find_element(By.LINK_TEXT, 'Form Authentication')

    @staticmethod
    def alert_locator(driver):
        return driver.find_element(By.LINK_TEXT, 'JavaScript Alerts')

    @staticmethod
    def dropdown_locator(driver):
        return driver.find_element(By.LINK_TEXT, 'Dropdown')

    @staticmethod
    def checkbox_locator(driver):
        return driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[6]/a')


base_locator_instance = BasePage()
