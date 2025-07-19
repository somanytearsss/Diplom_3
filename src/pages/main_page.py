import allure

from src.locators.main_page_locators import MainPageLocators
from src.pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной')
    def click_log_in_button_account(self):
        self.click_element(MainPageLocators.ENTER_MAIN_PAGE_SIGN_IN_BUTTON)

    @allure.step('Кликнуть по кнопке "Оформить заказ"')
    def click_place_on_order_button(self):
        self.click_element(MainPageLocators.PLACE_AN_ORDER_BUTTON)

    @allure.step('Кликнуть по кнопке "Лента заказов"')
    def click_feed_orders_button(self):
        self.find_element(MainPageLocators.BUTTON_FEED_ORDERS_HEADER)
        self.click_element(MainPageLocators.BUTTON_FEED_ORDERS_HEADER)

    @allure.step('Кликнуть по кнопке конструктора в хидере')
    def click_constructor_header_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.step('Кликнуть по ингредиенту в конструкторе')
    def click_ingredient_in_constructor(self):
        self.click_element(MainPageLocators.INGREDIENT_IN_CONSTRUCTOR)

    @allure.step('Проверка заголовка "Соберите бургер"')
    def check_make_burger_title(self):
        self.click_element(MainPageLocators.MAKE_BURGER_TITLE)

    @allure.step('Проверка появления окна "Детали ингредиента"')
    def check_popup_window_details(self):
        self.find_element(MainPageLocators.DETAILS_OF_INGREDIENT)
        return self.check_visible_of_element(MainPageLocators.DETAILS_OF_INGREDIENT)

    @allure.step('Проверка закрытия окна "Детали ингредиента"')
    def check_popup_window_details_closed(self):
        self.find_element(MainPageLocators.DETAILS_OF_INGREDIENT)
        return not self.check_visible_of_element(MainPageLocators.DETAILS_OF_INGREDIENT)

    @allure.step('Закрытие окна "Детали ингредиента"')
    def close_popup_window_details(self):
        self.click_element(MainPageLocators.CLOSE_POPUP_WINDOW_INGREDIENT)

    @allure.step('Перетаскивание ингредиента в корзину')
    def drag_and_drop_ingredient_to_basket(self):
        from_ingredient = self.find_element(MainPageLocators.INGREDIENT_IN_CONSTRUCTOR)
        to_ingredient = self.find_element(MainPageLocators.BURGER_CONSTRUCTOR)
        self.drag_and_drop_element(from_ingredient, to_ingredient)

    @allure.step('Получение числа добавленных ингредиентов')
    def get_count_ingredient_in_basket(self):
        return  self.get_text_from_element(MainPageLocators.COUNT_INGREDIENT)

    @allure.step('Закрытие окна "Заказ создан"')
    def close_popup_window_create_order(self):
        self.find_element(MainPageLocators.CLOSE_POPUP_WINDOW_AFTER_CREATE_ORDER)
        self.click_element(MainPageLocators.CLOSE_POPUP_WINDOW_AFTER_CREATE_ORDER)

    @allure.step('Получаем номер нового заказа')
    def get_order_number(self):
        element = self.find_element(MainPageLocators.MODAL_NEW_ORDER_NUMBER)
        return element.text

    @allure.step('Ожидание обновления номера заказа')
    def wait_order_created(self):
        order_number = "9999"
        while order_number == "9999":
            order_number = self.find_element(MainPageLocators.MODAL_NEW_ORDER_NUMBER).text
        return order_number