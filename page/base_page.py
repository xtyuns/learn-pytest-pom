from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Locator:
    def __init__(self, by: By, value: str):
        self.by = by
        self.value = value


class BasePage:
    def __init__(self, selenium: WebDriver):
        self.selenium = selenium

    def _pick_element(self, locator: Locator) -> WebElement:
        return self.selenium.find_element(locator.by, locator.value)

    def _do_input(self, locator: Locator, value):
        ele = self._pick_element(locator)
        ele.clear()
        ele.send_keys(value)

    def _do_click(self, locator: Locator):
        ele = self._pick_element(locator)
        ele.click()

    def _pick_text(self, locator: Locator) -> str:
        ele = self._pick_element(locator)
        return ele.text
