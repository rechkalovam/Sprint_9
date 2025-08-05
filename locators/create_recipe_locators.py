from selenium.webdriver.common.by import By
import data


class CreateRecipeLocators:
    CREATE_RECIPE_FORM = By.XPATH, "//form[contains(@class, 'styles_form')]"
    RECIPE_NAME_INPUT = By.XPATH, "//label[div[text()='Название рецепта']]/input"
    INGREDIENT_NAME_INPUT = By.XPATH, "//input[contains(@class, 'styles_ingredientsInput')]"
    FIRST_INGREDIENT_IN_DROPDOWN = By.XPATH, f'(//div[contains(text(), "{data.RECIPE_DATA["ingredient"]}")])[1]'
    INGREDIENT_AMOUNT_INPUT = By.XPATH, "//input[contains(@class, 'ingredientsAmountValue')]"
    ADD_INGREDIENT_BUTTON = By.XPATH, "//div[text()='Добавить ингредиент']"
    COOKING_TIME_INPUT = By.XPATH, "//label[div[text()='Время приготовления']]/input"
    RECIPE_DESCRIPTION_TEXTAREA = By.XPATH, "//textarea[contains(@class, 'textareaField')]"
    ADD_RECIPE_PHOTO_BUTTON = By.XPATH, "//input[@type='file']"
    CREATE_RECIPE_BUTTON = By.XPATH, "//button[text()='Создать рецепт' and not(@disabled)]"