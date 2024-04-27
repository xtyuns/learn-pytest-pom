from typing import Tuple

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.dologin
@pytest.mark.smoke
def test_login_with_valid_credentials(page: Page, credentials: Tuple[str, str]):
    p_username = credentials[0]
    p_password = credentials[1]

    page.goto("/login")

    login_input = page.get_by_label("帐号")
    login_input.click()
    login_input.fill(p_username)

    password_input = page.get_by_label("密码", exact=True)
    password_input.click()
    password_input.fill(p_password)

    page.get_by_role("button", name="登 录").click()

    expect(page.get_by_role("tooltip")).to_have_text(p_username)


def test_logined(page: Page):
    page.goto("/")
    expect(page.get_by_role("tooltip")).to_have_text("admin")
