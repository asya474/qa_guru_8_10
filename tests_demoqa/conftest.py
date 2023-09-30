import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_open():
    browser.config.window_width = 400
    browser.config.window_height = 620
    browser.open('https://demoqa.com/automation-practice-form')

    yield

    ...
