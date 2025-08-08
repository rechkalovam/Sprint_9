import allure
from pages.base_page import BasePage
from locators.recipe_page_locators import RecipePageLocators


class RecipePage(BasePage):
    @allure.step('Проверка отображения страницы рецепта')
    def check_visibility_of_recipe_page(self):
        return self.find_element_with_wait(RecipePageLocators.RECIPE_CARD_INFO)

    @allure.step('Проверка названия рецепта')
    def check_recipe_name(self):
        return self.get_text_from_element(RecipePageLocators.RECIPE_CARD_NAME)