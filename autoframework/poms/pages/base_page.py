from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        """Access specified URL."""
        self.driver.get(url)

    def click_element(self, locator, timeout=10):
        """Click on desired element. Raises TimeoutException if not found."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located((locator)))
            element = wait.until(EC.element_to_be_clickable((locator)))
            element.click()
        except TimeoutException:
            print(f"[ERROR] Timeout: element not clickable within {timeout}s: {locator}")
            raise

    def fill_text(self, locator, text, timeout=10):
        """Type text in field. Raises TimeoutException if element not found."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located((locator)))
            element = wait.until(EC.element_to_be_clickable((locator)))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            print(f"[ERROR] Timeout: field not editable within {timeout}s: {locator}")
            raise

    def get_presence_of_element(self, locator, timeout=10):
        """Get presence of element. Returns None if not found within timeout."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located((locator)))
            return element
        except TimeoutException:
            print(f"[WARN] Element not found within {timeout}s: {locator}")
            return None

    def get_presence_of_elements(self, locator, timeout=10):
        """Get presence of multiple elements. Returns empty list if none found within timeout."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            elements = wait.until(EC.visibility_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            print(f"[WARN] No elements found within {timeout}s: {locator}")
            return []
