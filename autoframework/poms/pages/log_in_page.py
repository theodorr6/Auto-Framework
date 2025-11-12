from autoframework.poms.pages.base_page import BasePage
from autoframework.poms.pages.home_page import HomePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    """POM for the log in page."""
    path = '/login'

    USERNAME = (By.ID, "username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    INVALID_PASS_ERROR = "//div[contains(text(),'{} is invalid')]"

    def __init__(self, base_url, driver):
        super().__init__(driver)
        self.url = base_url + self.path
        self.driver = driver

    def open(self):
        """Open login page."""
        self.driver.get(self.url)

    def type_username(self, username):
        """Type username in the login page, username field."""
        self.fill_text(self.USERNAME, username)

    def type_password(self, password):
        """Type password in the login page, password field."""
        self.fill_text(self.PASSWORD, password)

    def click_log_in_btn(self):
        """Click log in button."""
        self.click_element(self.LOGIN_BTN)
        return HomePage(self.driver)
    
    def get_presence_of_invalid_credentials_error(self, invalid_param):
        """Get presence of invalid password error."""
        locator = (By.XPATH, self.INVALID_PASS_ERROR.format(invalid_param))
        return self.get_presence_of_element(locator)