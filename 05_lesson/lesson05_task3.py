from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

sleep(2)
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("Sky")

sleep(2)
input_field.clear()

sleep(2)
input_field.send_keys("Pro")

sleep(5)
driver.quit()