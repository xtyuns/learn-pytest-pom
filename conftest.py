import os
from typing import Tuple, Optional

import pytest


def pytest_addoption(parser):
    # register credentials option
    group = parser.getgroup("authentication")
    group.addoption(
        "--credentials",
        nargs=2,
        metavar=('username', 'password'),
        dest="credentials",
        action="store",
        help='username and password for testing platform.',
    )


@pytest.fixture(scope="function")
def credentials(request) -> Optional[Tuple[str, str]]:
    # fixture credentials for dologin marker
    if request.node.get_closest_marker("dologin"):
        credentials = request.config.getoption("credentials")
        if credentials:
            return credentials[0], credentials[1]
        else:
            raise pytest.UsageError("--credentials option is missing")


def pytest_cmdline_main(config):
    # set default base-url
    if not config.option.base_url:
        config.option.base_url = "https://testing"


def pytest_configure(config):
    # register markers
    config.addinivalue_line(
        "markers", "dologin: save login state after execution"
    )
    config.addinivalue_line(
        "markers", "relogin: not reuse login state"
    )
    config.addinivalue_line(
        "markers", "smoke: mark as a smoke test item"
    )


def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is None and any(marker.name == "dologin" for marker in item.own_markers):
        # save login state
        page = item.funcargs.get("page")
        session_profile = page.evaluate("() => window.sessionStorage.getItem('profile')")
        os.environ["SESSION_PROFILE"] = session_profile

    if call.when == "setup" and not any(marker.name == "relogin" for marker in item.own_markers):
        # reuse login state
        session_profile = os.environ.get("SESSION_PROFILE")
        if session_profile:
            context = item.funcargs.get("context")
            context.add_init_script("""(profile => {
                                window.sessionStorage.setItem('profile', profile);
                            })('""" + session_profile + "')")
