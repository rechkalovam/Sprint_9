import allure
import urls
from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    @allure.step('Проверка отображения формы регистрации')
    def check_visibility_registration_form(self):
        return self.find_element_with_wait(RegistrationPageLocators.REGISTER_FORM)

    @allure.step('Заполнение формы регистрации и нажатие кнопки "Создать аккаунт"')
    def add_user_data_and_click_register_button(self, user_data):
        self.add_text_to_element(RegistrationPageLocators.FIRST_NAME_INPUT, user_data["first_name"])
        self.add_text_to_element(RegistrationPageLocators.LAST_NAME_INPUT, user_data["last_name"])
        self.add_text_to_element(RegistrationPageLocators.USERNAME_INPUT, user_data["username"])
        self.add_text_to_element(RegistrationPageLocators.EMAIL_INPUT, user_data["email"])
        self.add_text_to_element(RegistrationPageLocators.PASSWORD_INPUT, user_data["password"])
        self.click_to_element(RegistrationPageLocators.REGISTER_SUBMIT_BUTTON)
        self.wait_until_url_is_changed(urls.URL_LOGIN_PAGE)

    @allure.step('Регистрация пользователя')
    def register_user(self, user_data):
        self.check_visibility_registration_form()
        self.add_user_data_and_click_register_button(user_data)