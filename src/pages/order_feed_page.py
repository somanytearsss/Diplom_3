from src.pages.base_page import BasePage
from src.locators.order_feed_page_locators import OrderFeedPageLocators
import allure


class OrderFeedPage(BasePage):
	@allure.step('Ожидание отображения заголовка Ленты заказов')
	def wait_and_check_displayed_title_of_orders_list(self):
		self.find_element(OrderFeedPageLocators.TITLE_ORDER_FEED)
		return self.check_visible_of_element(OrderFeedPageLocators.TITLE_ORDER_FEED)

	@allure.step('Получить количество заказов за все время')
	def get_count_orders_all_time(self):
		element = self.find_element(OrderFeedPageLocators.COUNT_ORDERS_ALL_TIME)
		return int(element.text)


	@allure.step('Получить количество заказов за сегодня')
	def get_count_orders_today(self):
		element = self.find_element(OrderFeedPageLocators.COUNT_ORDERS_TODAY)
		return int(element.text)

	@allure.step('Получить номер заказа "В работе"')
	def get_number_from_order_in_work(self):
		return self.get_text_from_element(OrderFeedPageLocators.NUMBER_ORDER_IN_WORK)