from selenium.webdriver.common.by import By

class ResultPage:

    def __init__(self, browser):
        self._driver = browser

    def add_books(self):
        buy_buttons = self._driver.find_elements(By.CSS_SELECTOR, "._btn.btn-tocart.buy-link")
        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1

        return counter