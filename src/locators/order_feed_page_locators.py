from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    # Список всех заказов
    LIST_ALL_ORDER_FEED = By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]"
    # Заголовок ленты заказов
    TITLE_ORDER_FEED = By.XPATH, "//div[contains(@class, 'OrderFeed_orderFeed')]/h1"
    # Карточка первого Бургера
    FIRST_BURGER_CARD = By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')][1]"
    # Всплывающее окно с заказом
    MODAL_WINDOW = By.XPATH, "//div[contains(@class, 'Modal_orderBox')]"
    # Заголовок всплывающего окна
    TITLE_MODAL_WINDOW = By.XPATH, "//div[contains(@class, 'Modal_orderBox')]//h2"
    # Число заказов за всё время
    COUNT_ORDERS_ALL_TIME = By.XPATH, "//p[contains(., 'Выполнено за все время:')]/following-sibling::p[contains(@class, 'OrderFeed_number') and contains(@class, 'text_type_digits-large')]"
    # COUNT_ORDERS_ALL_TIME = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"
    # Число заказов за сегодня
    COUNT_ORDERS_TODAY = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    # Заказы в обработке
    ORDER_LIST_READY = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li"
    # Карточка заказа
    ORDER_CARD = By.XPATH, "//*[contains(@class, 'OrderHistory_listItem')]"
    # Заголовок карточки заказа
    TITLE_ORDER_CARD = By.XPATH, "//*[contains(@class, 'OrderHistory_listItem')]//h2"
    # Номер заказа на странице заказов
    NUMBER_ORDER_IN_FEED_PAGE = By.XPATH, ".//*[text()='{order_id}']"
    # Номер карточки заказа
    ID_ORDER_CARD = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]')
    # Номер заказа в работе
    NUMBER_ORDER_IN_WORK = (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]')