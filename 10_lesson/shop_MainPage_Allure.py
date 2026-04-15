from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    def __init__(self, driver):
        """
        Конструктор класса MainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавление товара с ID {product_id} в корзину")
    def add_to_cart(self, product_id: str) -> None:
        """
        Добавляет товар в корзину по ID кнопки.

        :param product_id: str — ID кнопки добавления товара.
        :return: None
        """
        self.wait.until(EC.element_to_be_clickable((By.ID, product_id))).click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины.

        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()

