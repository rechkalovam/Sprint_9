from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FORM = By.XPATH,"//form[contains(@class, 'styles_form')]"
    EMAIL_INPUT = By.XPATH,"//input[@type='text']"
    PASSWORD_INPUT = By.XPATH, "//input[@type='password']"
    LOGIN_SUBMIT_BUTTON = By.XPATH, "//button[text()='Войти']"
    REGISTER_BUTTON = By.XPATH, "//a[text()='Создать аккаунт']"
    LOGIN_BUTTON = By.XPATH, "//a[text()='Войти']"