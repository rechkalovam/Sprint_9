import pytest
from selenium.webdriver import Remote
import os
from selenium.webdriver.chrome.options import Options
from helpers import HelpersMethods
from urls import URL_MAIN_PAGE
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')

    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": False
    })

    driver = Remote(
        command_executor=os.getenv("SELENOID_URL", "http://selenoid:4444/wd/hub"),
        options=options
    )
    yield driver
    driver.quit()

@pytest.fixture()
def register_user(driver):
    user_data = HelpersMethods.generate_user_data()
    login_page = LoginPage(driver)
    login_page.go_to_url(URL_MAIN_PAGE)
    login_page.click_to_registration_button()
    registration_page = RegistrationPage(driver)
    registration_page.register_user(user_data)
    return driver, {
        "email" : user_data["email"],
        "password" : user_data["password"]
    }

@pytest.fixture()
def login_user(register_user):
    driver, user_data = register_user
    login_page = LoginPage(driver)
    login_page.login_user(user_data)
    return driver

