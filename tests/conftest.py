import pytest
from _pytest.fixtures import FixtureRequest
from selenium import webdriver


@pytest.fixture(scope="class", autouse=True)
def selenium_driver(request: FixtureRequest):
    selenium_driver = webdriver.Chrome()
    request.node._driver = selenium_driver
    request.cls.selenium_driver = selenium_driver
    yield selenium_driver
    # quit the selenium driver
    selenium_driver.quit()
