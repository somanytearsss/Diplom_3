from src.pages.account_page import AccountPage
from src.pages.main_page import MainPage
from src.pages.order_feed_page import OrderFeedPage
import allure


class TestOrderFeedPage:
    @allure.title("Проверка, что при создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_orders_module_all_time_counter_increases(self, driver, create_and_delete_user):
        email, password = create_and_delete_user
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        feed_page = OrderFeedPage(driver)
        main_page.click_log_in_button_account()
        account_page.send_email_password(email, password)
        account_page.click_login_button()
        main_page.click_feed_orders_button()
        orders_count_one = feed_page.get_count_orders_all_time()
        main_page.click_constructor_header_button()
        main_page.drag_and_drop_ingredient_to_basket()
        main_page.click_place_on_order_button()
        main_page.wait_order_created()
        main_page.close_popup_window_create_order()
        main_page.click_feed_orders_button()
        orders_count_two = feed_page.get_count_orders_all_time()
        assert orders_count_two > orders_count_one

    @allure.title("Проверка, что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_orders_module_day_counter_increases(self, driver, create_and_delete_user):
        email, password = create_and_delete_user
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        feed_page = OrderFeedPage(driver)
        main_page.click_log_in_button_account()
        account_page.send_email_password(email, password)
        account_page.click_login_button()
        main_page.click_feed_orders_button()
        orders_count_one = feed_page.get_count_orders_today()
        main_page.click_constructor_header_button()
        main_page.drag_and_drop_ingredient_to_basket()
        main_page.click_place_on_order_button()
        main_page.wait_order_created()
        main_page.close_popup_window_create_order()
        main_page.click_feed_orders_button()
        orders_count_two = feed_page.get_count_orders_today()
        assert orders_count_two > orders_count_one

    @allure.title("Проверка, что после оформления заказа его номер появляется в разделе «В работе»")
    def test_check_new_order_is_displaying(self, driver, create_and_delete_user):
        email, password = create_and_delete_user
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        feed_page = OrderFeedPage(driver)
        main_page.click_log_in_button_account()
        account_page.send_email_password(email, password)
        account_page.click_login_button()
        main_page.drag_and_drop_ingredient_to_basket()
        main_page.click_place_on_order_button()
        main_page.wait_order_created()
        new_order = main_page.get_order_number()
        main_page.close_popup_window_create_order()
        main_page.click_feed_orders_button()
        order_in_work = feed_page.get_number_from_order_in_work()
        assert int(new_order) == int(order_in_work)