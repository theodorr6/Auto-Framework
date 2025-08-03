import time

import pytest

from autoframework.poms.pages.create_account_page import CreateAccountPage
from autoframework.poms.pages.home_page import HomePage
from autoframework.poms.pages.login_page import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestRegister:

    url = 'https://automationexercise.com'

    def test_register_user(self):
        """Verify user can register."""
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        create_acc_page = CreateAccountPage(self.driver)


        home_page.access_url(self.url)

        home_page.click_consent()
        assert home_page.verify_homepage()

        home_page.click_login_button()

        login_page.verify_signup_text()
        login_page.type_username()
        login_page.type_email()
        login_page.click_sign_up()

        assert create_acc_page.verify_acc_info_title()

        create_acc_page.select_title()

        create_acc_page.type_password("Parola")

        time.sleep(5)

