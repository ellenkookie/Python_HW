from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    def __init__(self, driver):
        """
        Конструктор класса CartPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажатие кнопки Checkout")
    def checkout(self) -> None:
        """
        Нажимает кнопку Checkout для перехода к оформлению заказа.

        :return: None
        """
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
