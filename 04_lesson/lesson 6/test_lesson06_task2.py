from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_controls():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    # Ваш код здесь

    driver.quit()
    