from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGOUT_BUTTON = By.XPATH, "//a[text()='Выход']"
    CREATE_RECIPE_TAB = By.XPATH, "//a[text()='Создать рецепт']"