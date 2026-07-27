from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():

    driver = webdriver.Firefox()
    driver.get('https://www.saucedemo.com/')

    driver.find_element(
        By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    driver.find_element(
        By.CSS_SELECTOR, '#password').send_keys('secret_sauce')

    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains('inventory'))

    driver.find_element(
        By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()

    driver.find_element(
        By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()

    driver.find_element(
        By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Иван')

    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Иванов')

    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('111000')

    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    total_price = driver.find_element(By.CSS_SELECTOR, '.summary_total_label')

    total_text = total_price.text

    # как вычленить только цифры из всего текста поля?
    total_value = float(total_text.split('$')[1])

    assert total_value == 58.29, f"Ожидаемая сумма 58.29, но получена {
        total_value}"

    driver.quit()
