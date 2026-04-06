from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
   def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait (driver, 50)

   def open (self):
       self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

   def set_delay(self, seconds: int):
       delay_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
       delay_input.clear()
       delay_input.send_keys(str(seconds))

   def click_button(self, text: str):
       self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{text}']"))).click()

   def get_result(self, expected_result: str = None) -> str:
       self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), expected_result))
       return self.driver.find_element(By.CLASS_NAME, "screen").text