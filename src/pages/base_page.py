import allure
from selenium.webdriver import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from src.locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver


    @allure.step('Поиск элемента по локатору')
    def find_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Поиск элемента по локатору и клик по нему')
    def click_element(self, locator):
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Проверка ,что элемент кликабелен')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))

    @allure.step('Перетаcкивание элемента')
    def drag_and_drop_element(self, from_element, to_element):
        with allure.step(f"Перетаскиваем элемент от {from_element} в {to_element}"):
            ActionChains(self.driver).drag_and_drop(from_element, to_element).pause(5).perform()

    @allure.step('Проверка отображения элемента')
    def check_visible_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Получение текста из элемента')
    def get_text_from_element(self, locator):
        return self.find_element(locator).text

    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Ожидание удаления элемента со страницы')
    def wait_element_disappearing (self, locator):
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(locator))

    @allure.step('Ждем исчезновения оверлэй объекта - скролл')
    def wait_disappear_overlay_scroll(self):
        self.wait_element_disappearing(MainPageLocators.OVERLAY_SCROLL)

    @allure.step('Получаем URL страницы')
    def get_current_url_page(self):
        current_url = self.driver.current_url
        return current_url