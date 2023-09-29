from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage, Locator


class LoginPage(BasePage):
    username_locator = Locator(By.ID, 'cbi-input-user')
    password_locator = Locator(By.ID, 'cbi-input-password')
    submit_locator = Locator(By.CSS_SELECTOR, '.cbi-button.cbi-button-apply')
    error_msg_locator = Locator(By.CSS_SELECTOR, '.errorbox')

    def __init__(self, selenium: WebDriver, target_base_url: str):
        super().__init__(selenium)
        self.selenium.get(target_base_url)

    def login(self, username: str, password: str):
        self.do_input(self.username_locator, username)
        self.do_input(self.password_locator, password)
        self.do_click(self.submit_locator)

    def get_error_msg(self):
        return self.pick_text(self.error_msg_locator)
