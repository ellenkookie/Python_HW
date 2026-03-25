from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

cookie = {"name": "cookie_policy", "value": "1"}

def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    #Открыть labirint.ru
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)
    browser.refresh()

    # Найти все книги по слову Python.
    browser.find_element(By.ID, "search-field").send_keys('python')
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    # Добавить все книги в корзину.
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, "._btn.btn-tocart.buy-link")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    # Перейти в корзину.
    browser.get("https://www.labirint.ru/cart/")
    # Проверить, что счетчик товаров соответствует количеству добавленных книг.
    txt = browser.find_element(By.ID, "basket-default-prod-count2").text
    count = int(txt.split()[0])

    assert counter == count
    browser.quit()