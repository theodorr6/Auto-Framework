import pytest
from autoframework.poms.pages.log_in_page import LoginPage


@pytest.fixture()
def login_logout(base_url, init_driver):
    """Log in to website."""
    login_page = LoginPage(base_url, init_driver)
    login_page.open()
    login_page.type_username("tomsmith")
    login_page.type_password("SuperSecretPassword!")
    home_page = login_page.click_log_in_btn()
    yield home_page
    home_page.click_log_out()

@pytest.fixture()
def login_invalid_pass(base_url, init_driver):
    login_page = LoginPage(base_url, init_driver)
    login_page.open()
    login_page.type_username("tomsmith")
    login_page.type_password("negative")
    login_page.click_log_in_btn()
    return login_page

@pytest.fixture()
def login_invalid_user(base_url, init_driver):
    login_page = LoginPage(base_url, init_driver)
    login_page.open()
    login_page.type_username("negative")
    login_page.type_password("SuperSecretPassword!")
    login_page.click_log_in_btn()
    return login_page

