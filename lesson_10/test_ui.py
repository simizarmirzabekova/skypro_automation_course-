import allure
from calculator_page import CalculatorPage
from shop_pages import LoginPage, MainPage, CartPage, CheckoutPage

@allure.title("Тест работы калькулятора")
@allure.description("Проверяем, что калькулятор правильно выполняет сложение с задержкой")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(chrome_driver):
    with allure.step("Открываем страницу калькулятора и устанавливаем задержку"):
        calc_page = CalculatorPage(chrome_driver)
        calc_page.open()
        calc_page.set_delay("45")
    
    with allure.step("Выполняем сложение: 7 + 8"):
        calc_page.press_button("7")
        calc_page.press_button("+")
        calc_page.press_button("8")
        calc_page.press_button("=")
    
    with allure.step("Проверяем результат сложения"):
        result = calc_page.get_result()
        assert result == "15"


@allure.title("Тест оформления покупки в магазине")
@allure.description("Проверяем полный путь пользователя: логин -> добавление товаров -> оформление")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(firefox_driver):
    with allure.step("Авторизуемся в магазине"):
        login_page = LoginPage(firefox_driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавляем товары в корзину"):
        shop_page = MainPage(firefox_driver)
        shop_page.add_to_cart("Sauce Labs Backpack")
        shop_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        shop_page.add_to_cart("Sauce Labs Onesie")
    
    with allure.step("Переходим в корзину и оформляем заказ"):
        cart_page = shop_page.go_to_cart()
        # Добавьте сюда остальные шаги оформления, если они у вас есть в коде
        