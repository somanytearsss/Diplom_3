from selenium.webdriver.common.by import By


class MainPageLocators:
    # Вход по кнопке «Войти в аккаунт» на главной
    ENTER_MAIN_PAGE_SIGN_IN_BUTTON = By.XPATH, "//button[contains(@class,'button_button__33qZ0')]"
    # Кнопка оформить заказ
    PLACE_AN_ORDER_BUTTON = By.XPATH, "//button[ text()='Оформить заказ' ]"
    # Ссылка на личный кабинет в хидере
    PERSONAL_ACCOUNT_BUTTON = By.CSS_SELECTOR, "a.AppHeader_header__link__3D_hX[href='/account']"
    # Ссылка на восстановление пароля
    RESET_PASSWORD_LINK = By.XPATH, "//a[ text()='Восстановить пароль' ]"
    # Ссылка на конструктор в хидере
    CONSTRUCTOR_HEADER = By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va' ) and text()='Конструктор']"
    # Ссылка на ингредиент
    INGREDIENT_LINK = By.XPATH, "//p[contains(@class, 'BurgerIngredient_ingredient__text__yp3dH']) and text()='Флюоресцентная булка R2-D3']"
    # Ссылка на логотип стеллар бургер в хидере
    STELLAR_BURGER_HEADER = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']"
    # Кнопка лента заказов
    BUTTON_FEED_ORDERS_HEADER = By.XPATH, "//p[contains(., 'Лента Заказов')]"
    # BUTTON_FEED_ORDERS_HEADER = By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va' ) and text()='Лента Заказов']"
    # Текст в конструкторе "Лента Заказов"
    FEED_BUTTON = By.XPATH, "//p[contains(text(),'Лента Заказов')]"
    # Текст в конструкторе "Соберите бургер"
    MAKE_BURGER_TITLE = By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']"
    # Подробнее об ингредиентах
    DETAILS_OF_INGREDIENT = By.XPATH, "//p[contains(text(),'Калории,ккал')]"
    # Ингридиент из конструктора
    INGREDIENT_IN_CONSTRUCTOR = By.XPATH, "//img[@alt='Краторная булка N-200i']"
    # Закрытия окна об ингредиентах
    CLOSE_POPUP_WINDOW_INGREDIENT = (By.XPATH, '//section[contains(@class, '
									'"Modal_modal_opened")]//button[contains(@class, "close")]')
    # Конструктор бургеров
    BURGER_CONSTRUCTOR = By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__')]"
    # Подсчёт ингредиентов в корзине
    COUNT_INGREDIENT = By.XPATH, "//p[@class='counter_counter__num__3nue1'][contains(., '2')]"
    # Окно после создания заказа
    POPUP_WINDOW_ORDER = By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]/div[contains(@class, 'Modal_modal__container')]"
    # Закрытие окна после создания заказа
    CLOSE_MODAL_ORDER = By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]/*/button[contains(@class, 'Modal_modal__close_modified__3V5XS')]"
    # Окно загрузки
    LOADING = By.XPATH, "//img[contains(@class, 'Modal_modal__loading')]"
    # Крест закрывающий окно
    CLOSE_POPUP_WINDOW_AFTER_CREATE_ORDER = By.XPATH, ".//button[contains(@class,'Modal_modal__close_modified')]"
    # Номер заказа во всплывающем окне
    MODAL_NEW_ORDER_NUMBER = By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]"
    # Модальное окно с четырьмя девятками после сделанного 1 заказа
    NINES_IN_MOD_WIN_AFTER_CREATE_ORDER = By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2"

    OVERLAY_SCROLL = By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"

    OVERLAY_MODAL = By.XPATH, ".//img[contains(@class, 'Modal_modal__loading')]"