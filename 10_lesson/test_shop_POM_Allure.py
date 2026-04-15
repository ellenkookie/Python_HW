import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from shop_LoginPage_Allure import LoginPage
from shop_MainPage_Allure import MainPage
from shop_CartPage_Allure import CartPage
from shop_CheckoutPage_Allure import CheckoutPage
import allure


@pytest.fixture
def driver():
    """Фикстура для инициализации и завершения работы драйвера."""
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест оформления заказа в интернет-магазине")
@allure.description("Тест проверяет полный цикл покупки: авторизация, "
                    "добавление товаров, оформление заказа, итоговая сумма.")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    with allure.step("Открытие страницы авторизации"):
        login_page = LoginPage(driver)
        login_page.open()

    with allure.step("Авторизация с пользователем standard_user"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        main_page = MainPage(driver)
        main_page.add_to_cart("add-to-cart-sauce-labs-backpack")
        main_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
        main_page.add_to_cart("add-to-cart-sauce-labs-onesie")

    with allure.step("Переход в корзину"):
        main_page.go_to_cart()

    with allure.step("Нажатие кнопки Checkout"):
        cart_page = CartPage(driver)
        cart_page.checkout()

    with allure.step("Заполнение формы оформления заказа"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Elen", "Hayrapetyan", "123456")

    with allure.step("Нажатие кнопки Continue"):
        checkout_page.continue_checkout()

    with allure.step("Получение итоговой суммы"):
        total = checkout_page.get_total()

    with allure.step("Проверка итоговой суммы"):
        assert total == "Total: $58.29", \
            f"Ожидалось: Total: $58.29, получено: {total}"