from selenium.webdriver.common.by import By


class RecipePageLocators:
    RECIPE_CARD_INFO = By.XPATH, "//div[contains(@class, 'single-card__info')]"
    RECIPE_CARD_NAME = By.XPATH, "//h1"