import allure
import urls
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestLoginPage:
    @allure.title("Проверка авторизации пользователя")
    def test_login_user(self, register_user):
        driver, user_data = register_user
        login_page = LoginPage(driver)
        login_page.login_user(user_data)
        main_page = MainPage(driver)
        assert main_page.check_visibility_of_logout_button() and driver.current_url == urls.URL_RECIPES_PAGE, \
        f"Не удалось выполнить вход: видимость кнопки выхода = {main_page.check_visibility_of_logout_button()}, " \
        f"текущий URL = '{driver.current_url}', ожидаемый URL = '{urls.URL_RECIPES_PAGE}'"

