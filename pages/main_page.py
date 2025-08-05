import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Проверка отображения кнопки "Выйти"')
    def check_visibility_of_logout_button(self):
        return self.find_element_with_wait(MainPageLocators.LOGOUT_BUTTON)

    @allure.step('Нажатие на таб "Создать рецепт"')
    def click_to_create_recipe_tab(self):
        self.click_to_element(MainPageLocators.CREATE_RECIPE_TAB)
