   
from calculator_page import CalculatorPage
from shop_pages import LoginPage, MainShopPage, CartPage, CheckoutPage


def test_calculator(chrome_driver):

    calc_page = CalculatorPage(chrome_driver)
    


    
    calc_page.open()
    calc_page.set_delay("45")

    
    calc_page.press_button("7")
    calc_page.press_button("+")
    calc_page.press_button("8")
    calc_page.press_button("=")
    
    # time.sleep(46) - Убрали! Теперь ожидание "15" происходит внутри get_result()
    
    result = calc_page.get_result()
    assert result == "15"



def test_shop(firefox_driver):
    # 1. Логинимся (метод login() теперь сам нажимает кнопку входа)
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
