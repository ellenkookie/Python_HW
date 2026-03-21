from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

cookie = {"name": "cookie_policy", "value": "1"}

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def open_labirint():
    #Открыть labirint.ru
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)
    browser.refresh()

def search(term):
    # Найти все книги по слову Python.
    browser.find_element(By.ID, "search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

def add_books():
    # Добавить все книги в корзину.
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, "._btn.btn-tocart.buy-link")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    return counter

def go_to_cart():
    # Перейти в корзину.
    browser.get("https://www.labirint.ru/cart/")

def get_cart_counter():
    # Проверить, что счетчик товаров соответствует количеству добавленных книг.
    txt = browser.find_element(By.ID, "basket-default-prod-count2").text
    return int(txt.split()[0])

def close_driver():
    browser.quit()

def test_cart_counter():
    open_labirint()
    search('python')
    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    close_driver()
    assert added == cart_counter

# def test_empty_search():
#     open_labirint()
#     search('no book search term')
#     txt = browser.find_element(By.CSS_SELECTOR, "h1.index-top-title").text()
#     close_driver()
#     assert txt == "Все, что мы нашли в Лабиринте по запросу «no book search term»"