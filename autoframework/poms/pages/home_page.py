from autoframework.poms.pages.base_page import BasePage
from autoframework.utils import translate


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    CONFIRM_LOGIN = ""
    LOGIN_REGISTER_BUTTON = "//a[text()=' Signup / Login']"
    CONSENT_BTN = "//p[text()='Consimțământ']"
    HOME_BUTTON = "//a[contains(@style,'orange')]"

    def verify_homepage(self):
        """Verify homepage is visible."""
        return self.get_presence_of_element(self.HOME_BUTTON)

    def get_presence_of_confirm_message(self):
        """Verify the successful login message after login."""
        return self.get_presence_of_element(self.CONFIRM_LOGIN)

    def click_login_button(self):
        """Click on Sign up and Log in button."""
        self.click_element(self.LOGIN_REGISTER_BUTTON)

    def click_consent(self):
        """Click consent for cookies."""
        self.click_element(self.CONSENT_BTN)
