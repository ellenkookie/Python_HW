from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнение формы: Имя={first_name}, Фамилия={last_name}, Индекс={postal_code}")
    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму оформления заказа.

        :param first_name: str — имя.
        :param last_name: str — фамилия.
        :param postal_code: str — почтовый индекс.
        :return: None
        """
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys(first_name)
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "last-name"))
        ).send_keys(last_name)
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "postal-code"))
        ).send_keys(postal_code)

    @allure.step("Нажатие кнопки Continue")
    def continue_checkout(self) -> None:
        """
        Нажимает кнопку Continue для перехода к итоговой странице.

        :return: None
        """
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    @allure.step("Получение итоговой суммы заказа")
    def get_total(self) -> str:
        """
        Возвращает итоговую сумму заказа.

        :return: str — текст с итоговой суммой.
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text