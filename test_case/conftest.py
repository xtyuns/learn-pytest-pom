import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def target_base_url(request) -> str:
    return 'http://192.168.123.1'


@pytest.fixture(scope='class')
def selenium():
    """ selenium web driver with class scope
    """
    selenium = webdriver.Chrome()
    yield selenium
    selenium.quit()
