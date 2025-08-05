import allure
import urls
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from urls import URL_MAIN_PAGE
from helpers import HelpersMethods


class TestRegistrationPage:
    @allure.title("Проверка регистрации пользователя")
    def test_register_user(self, driver):
        user_data = HelpersMethods.generate_user_data()
        driver.get(URL_MAIN_PAGE)
        login_page = LoginPage(driver)
        login_page.click_to_registration_button()
        registration_page = RegistrationPage(driver)
        registration_page.register_user(user_data)
        assert login_page.check_visibility_login_form() and driver.current_url == urls.URL_LOGIN_PAGE, \
        f"Не удалось завершить регистрацию: форма логина отображается = {login_page.check_visibility_login_form()}, " \
        f"текущий URL = '{driver.current_url}', ожидаемый URL = '{urls.URL_LOGIN_PAGE}'"