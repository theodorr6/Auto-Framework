from autoframework.poms.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class ElementsPage(BasePage):
    """POM for the elements page."""
    path = "/add_remove_elements/"

    ADD_ELEMENT_BTN = (By.XPATH, "//button[text()='Add Element']")
    DELETE_ELEMENT_BTN = (By.XPATH, "//button[text()='Delete']")

    def __init__(self, base_url, driver):
        super().__init__(driver)
        self.url = base_url + self.path
        self.driver = driver

    def open(self):
        """Open login page."""
        self.driver.get(self.url)

    def add_elements(self, count=1):
        """Click add element button."""
        for _ in range(count):
            self.click_element(self.ADD_ELEMENT_BTN)
    
    def delete_element(self):
        """Click delete element button."""
        self.click_element(self.DELETE_ELEMENT_BTN)

    def count_delete_elements(self):
        """Get the total amount of delete elements."""
        elements = self.driver.find_elements(*self.DELETE_ELEMENT_BTN)
        return len(elements)