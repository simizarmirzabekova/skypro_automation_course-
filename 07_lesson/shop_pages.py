from selenium.webdriver.common.by import By

# 1. Страница авторизации
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)

    def login(self, username: str, password: str):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

# 2. Главная страница магазина
class MainShopPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, item_name: str):
        # Формируем ID кнопки на основе названия товара (заменяем пробелы на дефисы и приводим к нижнему регистру)
        item_id = f"add-to-cart-{item_name.lower().replace(' ', '-')}"
        self.driver.find_element(By.ID, item_id).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# 3. Страница корзины
class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

# 4. Страница оформления заказа (Checkout)
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_price(self) -> str:
        # Находим элемент с итоговой суммой (Total)
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        return total_element.text
    