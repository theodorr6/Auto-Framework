from autoframework.poms.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    """POM for the home page."""

    SECURE_AREA = (By.XPATH, "//h2[text()=' Secure Area']")
    LOGOUT_BTN = (By.XPATH, "//i[text()=' Logout']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_secure_area_presence(self):
        """Verify the presence of the secure area after login."""
        return self.get_presence_of_element(self.SECURE_AREA)

    def click_log_out(self):
        """Click the log out button."""
        self.click_element(self.LOGOUT_BTN)