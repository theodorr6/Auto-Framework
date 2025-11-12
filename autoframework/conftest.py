import pytest
from selenium import webdriver
import os

os.environ['BROWSER']='chrome'
os.environ['HEADLESS']='false'

@pytest.fixture(scope="class")
def init_driver():
    supported_browsers = ['chrome', 'firefox', 'safari']

    browser = os.getenv('BROWSER', 'chrome').lower()
    headless = os.getenv('HEADLESS', 'false').lower() == 'true'

    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not supported!"
                        f"Supported browsers: {supported_browsers}")


    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)

    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()

    elif browser == 'safari':
        options = webdriver.SafariOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Safari(options=options)
        driver.maximize_windows()

    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    """Base URL for application."""
    return os.getenv('BASE_URL', 'https://the-internet.herokuapp.com')