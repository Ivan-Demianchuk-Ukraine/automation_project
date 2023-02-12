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


class AuthPage:

    @staticmethod
    def username_locator(driver):
        return driver.find_element(By.ID, 'username')

    @staticmethod
    def password_locator(driver):
        return driver.find_element(By.ID, 'password')

    @staticmethod
    def submit_button(driver):
        return driver.find_element(By.XPATH, '//*[@id="login"]/button/i')


auth_instance = AuthPage()


class AlertPage:

    @staticmethod
    def confirm_alert_link_locator(driver):
        return driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')


alert_instance = AlertPage()


class CheckboxPage:

    @staticmethod
    def checkbox_option_1(driver):
        return driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')

    @staticmethod
    def checkbox_option_2(driver):
        return driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')


checkbox_instance = CheckboxPage()


class DropdownPage:

    @staticmethod
    def dropdown(driver):
        return driver.find_element(By.ID, 'dropdown')

    @staticmethod
    def dropdown_option_1(driver):
        return driver.find_element(By.XPATH, '//*[@id="dropdown"]/option[2]')

    @staticmethod
    def dropdown_option_2(driver):
        return driver.find_element(By.XPATH, '//*[@id="dropdown"]/option[3]')


dropdown_instance = DropdownPage()
