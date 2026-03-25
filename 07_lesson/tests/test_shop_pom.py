import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.shop_LoginPage import LoginPage
from pages.shop_MainPage import MainPage
from pages.shop_CartPage import CartPage
from pages.shop_CheckoutPage import CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shop(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    main_page = MainPage(driver)
    main_page.add_to_cart("add-to-cart-sauce-labs-backpack")
    main_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    main_page.add_to_cart("add-to-cart-sauce-labs-onesie")
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Elen", "Hayrapetyan", "123456")
    checkout_page.continue_checkout()

    total = checkout_page.get_total()
    assert total == "Total: $58.29"