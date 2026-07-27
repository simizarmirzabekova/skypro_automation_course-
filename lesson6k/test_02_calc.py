from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():

    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    input = driver.find_element(By.CSS_SELECTOR, '#delay')
    input.clear()
    input.send_keys("45")

    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()

    wait = WebDriverWait(driver, 45)
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".screen"), "15"))

    screen = driver.find_element(By.CSS_SELECTOR, '.screen')
    screen_txt = screen.text

    assert '15' in screen_txt

    print("Тест пройден успешно: результат — 15")

    driver.quit()
