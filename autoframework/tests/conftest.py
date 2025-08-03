import pytest

from autoframework.poms.pages.home_page import HomePage
from autoframework.poms.pages.login_page import LoginPage


@pytest.fixture()
def log_in(request):
    """Log in to website."""
    driver = request.cls.driver
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    login_page.access_url("https://automationexercise.com/login")
    home_page.click_consent()
    login_page.type_username()
    login_page.type_password()
    login_page.click_submit_button()
    return home_page

