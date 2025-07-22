from src.pages.base_page import BasePage
import allure
from src.locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    @allure.step('Ввод Email и пароля')
    def send_email_password(self, email, password):
        self.send_keys_to_input(AccountPageLocators.EMAIL_INPUT_FIELD_LOGIN, email)
        self.send_keys_to_input(AccountPageLocators.PASSWORD_INPUT_FIELD_LOGIN, password)

    @allure.step('Кликнуть по кнопке "Войти"')
    def click_login_button(self):
        self.click_element(AccountPageLocators.LOGIN_BUTTON)