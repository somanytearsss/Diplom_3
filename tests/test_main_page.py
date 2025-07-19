import allure
from src.pages.main_page import MainPage
from src.pages.order_feed_page import OrderFeedPage
from src.config import Urls


class TestMainPage:
    @allure.title("Проверка перехода по клику на Конструктор")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.wait_disappear_overlay_scroll()
        main_page.click_log_in_button_account()
        main_page.click_constructor_header_button()
        assert main_page.get_current_url_page() == Urls.MAIN_URL

    @allure.title("Проверка перехода по клику на Ленту заказов")
    def test_go_to_feed_orders_list(self, driver):
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)
        main_page.click_feed_orders_button()
        assert feed_page.wait_and_check_displayed_title_of_orders_list()

    @allure.title("Проверка появления всплывающего окна c деталями после клика на ингредиент")
    def test_show_popup_window_after_click_to_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient_in_constructor()
        assert main_page.check_popup_window_details()

    @allure.title("Проверка закрытия всплывающего окна по крестику")
    def test_close_popup_window_after_click_close_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient_in_constructor()
        main_page.close_popup_window_details()
        assert main_page.check_popup_window_details_closed() is False

    @allure.title("Проверка, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_add_ingredient_and_count_ingredient_increases(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient_to_basket()
        assert main_page.get_count_ingredient_in_basket() != 0