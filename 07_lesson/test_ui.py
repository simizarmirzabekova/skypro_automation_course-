import time
from calculator_page import CalculatorPage
from shop_pages import LoginPage, MainShopPage, CartPage, CheckoutPage

# ТЕСТ 1. Калькулятор (используем chrome_driver)
def test_calculator(chrome_driver):
    # 1. Создаем объект страницы
    calc_page = CalculatorPage(chrome_driver)
    
    # 2. Открываем страницу и вводим задержку
    calc_page.open()
    calc_page.set_delay("45")
    
    # 3. Нажимаем кнопки (7 + 8 =)
    calc_page.press_button("7")
    calc_page.press_button("+")
    calc_page.press_button("8")
    calc_page.press_button("=")
    
    # 4. Ждем результат (ставим небольшую паузу, так как реально ждать 45 секунд долго, 
    # но для автотеста нужно убедиться, что он дождется. 
    # Используем таймер, чтобы тест не висел 45 секунд, если что-то пойдет не так).
    # В реальном проекте лучше использовать WebDriverWait, но здесь сделаем просто:
    time.sleep(46) 
    
    # 5. Проверяем результат
    assert calc_page.get_result() == "15"


# ТЕСТ 2. Интернет-магазин (используем firefox_driver)
def test_shop(firefox_driver):
    # 1. Логинимся
    login_page = LoginPage(firefox_driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    # 2. Добавляем товары
    shop_page = MainShopPage(firefox_driver)
    shop_page.add_to_cart("Sauce Labs Backpack")
    shop_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    shop_page.add_to_cart("Sauce Labs Onesie")
    
    # 3. Переходим в корзину и нажимаем Checkout
    shop_page.go_to_cart()
    cart_page = CartPage(firefox_driver)
    cart_page.checkout()
    
    # 4. Заполняем форму
    checkout_page = CheckoutPage(firefox_driver)
    checkout_page.fill_form("Ivan", "Petrov", "123456")
    
    # 5. Проверяем итоговую стоимость
    total = checkout_page.get_total_price()
    assert total == "Total: $58.29"
    