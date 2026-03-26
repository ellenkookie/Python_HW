from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
   def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(driver, 10)

   def fill_form(self, first_name: str, last_name: str, postal_code: str):
       self.wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(first_name)
       self.wait.until(EC.visibility_of_element_located((By.ID, "last-name"))).send_keys(last_name)
       self.wait.until(EC.visibility_of_element_located((By.ID, "postal-code"))).send_keys(postal_code)

   def continue_checkout(self):
       self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

   def get_total(self) -> str:
       total_element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
       return total_element.text