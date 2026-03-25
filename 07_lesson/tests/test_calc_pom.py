import pytest
from selenium import webdriver
from pages.calcPage import CalcPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator(driver):
    calc = CalcPage(driver)
    calc.open()
    calc.set_delay(45)

    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")

    result = calc.get_result()
    assert result == "15"