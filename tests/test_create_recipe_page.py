import allure
import data
from pages.create_recipe_page import CreateRecipePage
from pages.main_page import MainPage
from pages.recipe_page import RecipePage


class TestCreateRecipePage:
    @allure.title("Проверка создания рецепта")
    def test_create_recipe(self, login_user):
        main_page = MainPage(login_user)
        main_page.click_to_create_recipe_tab()
        create_recipe_page = CreateRecipePage(login_user)
        create_recipe_page.create_recipe()
        recipe_page = RecipePage(login_user)
        assert recipe_page.check_visibility_of_recipe_page() and recipe_page.check_recipe_name() == data.RECIPE_DATA["name"], \
            f"Создание рецепта не удалось: видимость страницы = {recipe_page.check_visibility_of_recipe_page()}, " \
            f"ожидаемое имя = '{data.RECIPE_DATA['name']}', фактическое имя = '{recipe_page.check_recipe_name()}'"

