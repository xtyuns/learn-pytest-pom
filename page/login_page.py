from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page.base_page import BasePage, Locator


class LoginPage(BasePage):
    __username_locator = Locator(By.ID, 'cbi-input-user')
    __password_locator = Locator(By.ID, 'cbi-input-password')
    __submit_locator = Locator(By.CSS_SELECTOR, '.cbi-button.cbi-button-apply')
    __error_msg_locator = Locator(By.CSS_SELECTOR, '.errorbox')

    def __init__(self, selenium: WebDriver, target_base_url: str):
        super().__init__(selenium)
        self.selenium.get(target_base_url)

    def login(self, username: str, password: str):
        self._do_input(self.__username_locator, username)
        self._do_input(self.__password_locator, password)
        self._do_click(self.__submit_locator)

    def get_error_msg(self):
        return self._pick_text(self.__error_msg_locator)
