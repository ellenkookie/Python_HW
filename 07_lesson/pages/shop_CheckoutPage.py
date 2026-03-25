from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def continue_checkout(self):
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text