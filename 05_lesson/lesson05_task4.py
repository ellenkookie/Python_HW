from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

input_field = driver.find_element(By.NAME, "username")
input_field.send_keys("tomsmith")
sleep(2)

input_field = driver.find_element(By.NAME, "password")
input_field.send_keys("SuperSecretPassword!")
sleep(2)

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
sleep(2)

flash_text = driver.find_element(By.CLASS_NAME, "flash").text
print(flash_text)

sleep(5)
driver.quit()