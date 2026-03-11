# 3) Дождаться картинки
# Напишите скрипт.
# Шаги:
# Перейдите на сайт https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
# Дождитесь загрузки всех картинок.
# Получите значение атрибута src у 3-й картинки.
# Выведите значение в консоль.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 30)
wait.until(
    EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
)

#Вариант 1: поиск третьей картинки по индексу (точнее соответствует заданию)
container = driver.find_element(By.CSS_SELECTOR, "#image-container")
images = container.find_elements(By.TAG_NAME, "img")
third_image = images[2]
print(third_image.get_attribute("src"))

#Вариант 2: поиск по конкретному ID (проще, но привязан к id="award")
# award_image = wait.until(
#     EC.presence_of_element_located((By.ID, "award"))
# )
# src_value = award_image.get_attribute("src")
# print(src_value)

driver.quit()
