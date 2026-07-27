from selenium.webdriver import WebDriver


class ShopMainPage:
    """Главная страница интернет-магазина."""

    CART_ICON_LOCATOR = '#shopping_cart_container a'

    PRODUCT_BACKPACK_ADD_BUTTON = '[data-test="add-to-cart-sauce-labs-backpack"]'
    PRODUCT_TSHIRT_ADD_BUTTON = '[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]'
    PRODUCT_ONESIE_ADD_BUTTON = '[data-test="add-to-cart-sauce-labs-onesie"]'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_backpack_to_cart(self) -> None:
        """Добавляет товар Backpack в корзину."""
        btn = self.driver.find_element(By.CSS_SELECTOR, self.PRODUCT_BACKPACK_ADD_BUTTON)
        btn.click()

    def add_tshirt_to_cart(self) -> None:
        """Добавляет товар Bolt T-Shirt в корзину."""
        btn = self.driver.find_element(By.CSS_SELECTOR, self.PRODUCT_TSHIRT_ADD_BUTTON)
        btn.click()

    def add_onesie_to_cart(self) -> None:
        """Добавляет товар Onesie в корзину."""
        btn = self.driver.find_element(By.CSS_SELECTOR, self.PRODUCT_ONESIE_ADD_BUTTON)
        btn.click()

    def go_to_cart(self) -> None:
        """Переходит в Корзину через иконку в шапке сайта."""
        cart_icon = self.driver.find_element(By.CSS_SELECTOR, self.CART_ICON_LOCATOR)
        cart_icon.click()
        