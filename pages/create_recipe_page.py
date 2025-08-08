import allure
from pages.base_page import BasePage
from locators.create_recipe_locators import CreateRecipeLocators
import data


class CreateRecipePage(BasePage):
    @allure.step('Проверка отображения формы создания рецепта')
    def check_visibility_of_create_recipe_form(self):
        return self.find_element_with_wait(CreateRecipeLocators.CREATE_RECIPE_FORM)

    @allure.step('Заполнение поля названия рецепта')
    def add_recipe_name(self):
        self.add_text_to_element(CreateRecipeLocators.RECIPE_NAME_INPUT, data.RECIPE_DATA["name"])

    @allure.step('Добавление ингредиента в рецепт')
    def add_recipe_ingredient(self):
        self.add_text_to_element(CreateRecipeLocators.INGREDIENT_NAME_INPUT, data.RECIPE_DATA["ingredient"])
        self.click_to_element(CreateRecipeLocators.FIRST_INGREDIENT_IN_DROPDOWN)
        self.add_text_to_element(CreateRecipeLocators.INGREDIENT_AMOUNT_INPUT, data.RECIPE_DATA["amount"])
        self.click_to_element(CreateRecipeLocators.ADD_INGREDIENT_BUTTON)

    @allure.step('Заполнение поля времени приготовления рецепта')
    def add_recipe_cooking_time(self):
        self.add_text_to_element(CreateRecipeLocators.COOKING_TIME_INPUT, data.RECIPE_DATA["cooking_time"])

    @allure.step('Заполнение поля описания рецепта')
    def add_recipe_description(self):
        self.add_text_to_element(CreateRecipeLocators.RECIPE_DESCRIPTION_TEXTAREA, data.RECIPE_DATA["description"])

    @allure.step('Добавление фото в рецепт')
    def add_recipe_photo(self):
        self.add_photo_to_uploader(CreateRecipeLocators.ADD_RECIPE_PHOTO_BUTTON, data.RECIPE_DATA["photo"])

    @allure.step('Нажатие кнопки создания рецепта')
    def click_add_recipe_button(self):
        self.click_to_element(CreateRecipeLocators.CREATE_RECIPE_BUTTON)

    @allure.step('Создание рецепта')
    def create_recipe(self):
        self.check_visibility_of_create_recipe_form()
        self.add_recipe_name()
        self.add_recipe_ingredient()
        self.add_recipe_cooking_time()
        self.add_recipe_description()
        self.add_recipe_photo()
        self.click_add_recipe_button()
