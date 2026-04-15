from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    def __init__(self, driver):
        """
        Конструктор класса LoginPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы авторизации")
    def open(self) -> None:
        """
        Открывает страницу авторизации SauceDemo.

        :return: None
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация с логином {username}")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию на сайте.

        :param username: str — имя пользователя.
        :param password: str — пароль.
        :return: None
        """
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        ).send_keys(password)
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        ).click()