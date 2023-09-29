import pytest
from selenium.common import NoSuchElementException

from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def login_page(selenium, target_base_url):
    login_page = LoginPage(selenium, target_base_url)
    yield login_page


class TestLoginPage:
    @pytest.mark.smoke
    def test_login_failed(self, login_page):
        login_page.login('root', 'any')
        error_msg = login_page.get_error_msg()
        assert error_msg == '无效的用户名和/或密码！请重试。'

    @pytest.mark.smoke
    def test_login_success(self, login_page):
        login_page.login('root', 'root')
        with pytest.raises(NoSuchElementException):
            login_page.get_error_msg()
