from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def wait_until_url_is_changed(self, url):
        return self.wait.until(expected_conditions.url_to_be(url))

    def add_photo_to_uploader(self, locator, photo):
        self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(photo)