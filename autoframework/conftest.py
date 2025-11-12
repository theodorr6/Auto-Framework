import pytest
from selenium import webdriver
import os
from autoframework import env

@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ['chrome', 'firefox', 'safari']

    browser = os.getenv('BROWSER', 'chrome')
    print(f"BROWSER environment variable: {browser}")
    if not browser:
        raise Exception("Please select a browser!")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not supported!"
                        f"Supported browsers: {supported_browsers}")


    if browser in 'chrome':
        driver = webdriver.Chrome()
    elif browser in 'firefox':
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    driver.quit()