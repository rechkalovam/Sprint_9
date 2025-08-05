import allure

import urls
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    @allure.step('Нажатие кнопки "Войти"')
    def click_login_button(self):
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Проверка отображения формы авторизации пользователя')
    def check_visibility_login_form(self):
        return self.find_element_with_wait(LoginPageLocators.LOGIN_FORM)

    @allure.step('Нажатие кнопки "Создать аккаунт"')
    def click_to_registration_button(self):
        self.click_to_element(LoginPageLocators.REGISTER_BUTTON)

    @allure.step('Заполнение полей email и пароля и нажатие кнопки авторизации')
    def add_user_data_and_click_login_button(self, user_data):
        self.add_text_to_element(LoginPageLocators.EMAIL_INPUT, user_data["email"])
        self.add_text_to_element(LoginPageLocators.PASSWORD_INPUT, user_data["password"])
        self.click_to_element(LoginPageLocators.LOGIN_SUBMIT_BUTTON)
        self.wait_until_url_is_changed(urls.URL_RECIPES_PAGE)

    @allure.step('Авторизация пользователя')
    def login_user(self, user_data):
        self.click_login_button()
        self.check_visibility_login_form()
        self.add_user_data_and_click_login_button(user_data)