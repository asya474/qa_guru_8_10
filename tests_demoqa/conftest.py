import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.window_width = 393
    browser.config.window_height = 851
    browser.config.base_url = "https://demoqa.com"
    browser.config.timeout = 6.0

    yield

    browser.quit()
