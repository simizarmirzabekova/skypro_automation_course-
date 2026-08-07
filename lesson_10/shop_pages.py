from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)

    def login(self, username: str, password: str):
        """
        Выполняет вход в систему с указанными учетными данными.
        :param username: str - имя пользователя (например, "standard_user")
        :param password: str - пароль пользователя (например, "secret_sauce")
        :return: None
        """
        # ваш код логина


class MainShopPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, item_name: str):
        """
        Добавляет товар в корзину по его названию.
        :param product_name: str - название товара (например, "Sauce Labs Backpack")
        :return: None
        """
        # ваш код добавления товара
      

    def go_to_cart(self):
        """
        Переходит на страницу корзины.
        :return: CartPage - объект страницы корзины (для дальнейших действий)
        """
        # ваш код перехода в корзину и возврата страницы

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_price(self) -> str:

        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        return total_element.text
    