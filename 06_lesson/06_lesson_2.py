# 2) Переименовать кнопку
# Напишите скрипт.
# Шаги:
# Перейдите на сайт http://uitestingplayground.com/textinput.
# Укажите в поле ввода текст SkyPro.
# Нажмите на синюю кнопку.
# Получите текст кнопки и выведите в консоль ("SkyPro").

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

input_text = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_text.clear()
input_text.send_keys("SkyPro")

ub = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
ub.click()
print(ub.text)

driver.quit()
