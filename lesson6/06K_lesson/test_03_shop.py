import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.skipif(
    pytest.config.getoption("--browser") != "firefox",
    reason="Test requires FireFox"
)
def test_shop():
    """Автотест покупки"""

    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Авторизация
        driver.get("https://www.saucedemo.com/")
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        # 2. Добавление товаров в корзину
        items_to_buy = [
            ("Sauce Labs Backpack", By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']"),
            ("Sauce Labs Bolt T-Shirt", By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']"),
            ("Sauce Labs Onesie", By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-onesie']"),
        ]

        for item_name, by_type, locator in items_to_buy:
            # Ищем товар по названию
            product_card = driver.find_element(By.XPATH, f"//div[@class='inventory_item_name' and text()='{item_name}']/ancestor::div[@class='inventory_item']")
            # Находим кнопку добавления внутри карточки товара
            add_to_cart_button = product_card.find_element(by_type, locator)
            add_to_cart_button.click()

        # Переход в корзину
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        # 3. Оформление заказа
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Заполнение данных
        first_name_field = driver.find_element(By.ID, "first-name")
        last_name_field = driver.find_element(By.ID, "last-name")
        postal_code_field = driver.find_element(By.ID, "postal-code")
        continue_button = driver.find_element(By.ID, "continue")

        first_name_field.send_keys("Имя")
        last_name_field.send_keys("Фамилия")
        postal_code_field.send_keys("12345")
        continue_button.click()

        # 4. Получение итоговой суммы
        total_label = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_price = float(total_label.text.split("$")[1])

        # Закрытие браузера
        # Мы закрываем его здесь, чтобы проверить сумму до закрытия сессии
        driver.quit()

        # 5. Проверка
        # Сумма должна быть $58.29
        assert total_price == 58.29, f"Сумма неверна: {total_price}"

    except Exception as e:
        # Если что-то пошло не так, делаем скриншот ошибки
        timestamp = int(time.time())
        screenshot_path = f"error_{timestamp}.png"
        driver.save_screenshot(screenshot_path)
        print(f"\nСкриншот ошибки сохранён как: {screenshot_path}")
        raise e
    