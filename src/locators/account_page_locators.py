from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Кнопка входа в аккаунт
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']"
    # Поле ввода email
    EMAIL_INPUT_FIELD_LOGIN = By.XPATH, "//input[@name='name']"
    # Поле ввода пароля
    PASSWORD_INPUT_FIELD_LOGIN = By.XPATH, "//input[@name='Пароль']"