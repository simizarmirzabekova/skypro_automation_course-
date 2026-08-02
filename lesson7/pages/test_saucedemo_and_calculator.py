import time

import pytest

from selenium import webdriver

from selenium.webdriver.common.by import By

# Импортируем наши новые классы страниц
from pages.calculator_page import CalculatorPage
from pages.login_page import LoginPage
from pages.shop_cart_page import ShopCartPage
from pages.shop_checkout_page import ShopCheckoutPage
from pages.shop_main_page import ShopMainPage


import time
import pytest
from selenium import webdriver
# Импортируем наши новые классы страниц
from ..pages.calculator_page import CalculatorPage
from ..pages.login_page import LoginPage
from ..pages.shop_cart_page import ShopCartPage
from ..pages.shop_checkout_page import ShopCheckoutPage
from ..pages.shop_main_page import ShopMainPage


@pytest.fixture(scope='function')
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')  # Максимизировать окно
    with webdriver.Chrome(options=options) as driver:
        yield driver
        driver.quit()

def test_calculator_with_page_object(chrome_driver):
    """Тест проверяет работу калькулятора с использованием PageObject."""
    page = CalculatorPage(chrome_driver)

    # Шаг 1: Открываем страницу и задаем задержку
    page.open()
    page.set_delay(45)

    # Шаг 2: Вычисляем выражение 7 + 8
    page.click_button('7')
    page.click_button('+')
    page.click_button('8')
    page.click_button('=')

    # Ждем ровно 45 секунд, пока появится результат
    time.sleep(46)  # Добавили еще секунду "запас"

    # Проверяем результат
    result = page.get_result()
    assert result == 15, f"Ожидалось 15, но получено {result}"


def test_shop_flow_with_page_objects(firefox_driver):
    """Полный сценарий покупки товаров в магазине с использованием PageObject."""
    
    # Авторизация
    login_page = LoginPage(firefox_driver)
    login_page.open()
    login_page.enter_credentials('standard_user', 'secret_sauce')

    # Покупка товаров
    shop_page = ShopMainPage(firefox_driver)
    shop_page.add_backpack_to_cart()
    shop_page.add_tshirt_to_cart()
    shop_page.add_onesie_to_cart()
    shop_page.go_to_cart()

    # Оформление заказа
    cart_page = ShopCartPage(firefox_driver)
    cart_page.proceed_to_checkout()

    checkout_page = ShopCheckoutPage(firefox_driver)
    checkout_page.fill_form('Иван', 'Иванов', '12345')
    checkout_page.continue_to_overview()

    # Проверка суммы
    expected_total = 58.29
    actual_total = checkout_page.get_total_price()
    assert actual_total == expected_total, \
        f"Сумма неверная. Ожидается ${expected_total}, а получен ${actual_total}"
    