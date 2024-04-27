from typing import Tuple

import pytest
from playwright.sync_api import Page, expect

from tests.models.login import LoginPage


@pytest.mark.dologin
@pytest.mark.smoke
def test_login_with_valid_credentials(page: Page, credentials: Tuple[str, str]):
    p_username = credentials[0]
    p_password = credentials[1]

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.input_username(p_username)
    login_page.input_password(p_password)
    login_page.login()

    expect(page.get_by_role("tooltip")).to_have_text(p_username)


def test_logined(page: Page):
    page.goto("/")
    expect(page.get_by_role("tooltip")).to_have_text("admin")
