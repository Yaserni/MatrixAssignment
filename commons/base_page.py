import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self, *args):
        self.driver = args[0]
        self.wait = WebDriverWait(self.driver, 40)
        self.driver.set_page_load_timeout(90)
        self.WAITING_AFTER_CLICK = 0.5

    def element_by_id(self, element_id, wait=True):
        if wait:
            return self.wait.until(ec.presence_of_element_located((By.ID, element_id)))
        return self.driver.find_element_by_id(element_id)

    def element_by_css(self, element_css, wait=True):
        if wait:
            return self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, element_css)))
        return self.driver.find_element_by_css_selector(element_css)

    def elements_by_css(self, element_css, wait=True, wait_time=None):
        if wait:
            if wait_time is not None:
                return WebDriverWait(self.driver, wait_time).until(
                    ec.presence_of_all_elements_located((By.CSS_SELECTOR, element_css)))
            return self.wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, element_css)))
        return self.driver.find_elements_by_css_selector(element_css)

    def click_element(self, element):
        element.click()
        time.sleep(self.WAITING_AFTER_CLICK)

    def navigate_to_url(self, base_url):
        self.driver.get(base_url)
