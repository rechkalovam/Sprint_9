from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    REGISTER_FORM = By.XPATH, "//form[contains(@class, 'styles_form')]"
    FIRST_NAME_INPUT = By.XPATH, "//input[@name='first_name']"
    LAST_NAME_INPUT = By.XPATH, "//input[@name='last_name']"
    USERNAME_INPUT = By.XPATH, "//input[@name='username']"
    EMAIL_INPUT = By.XPATH, "//input[@name='email']"
    PASSWORD_INPUT = By.XPATH, "//input[@type='password']"
    REGISTER_SUBMIT_BUTTON = By.XPATH, "//button[text()='Создать аккаунт']"