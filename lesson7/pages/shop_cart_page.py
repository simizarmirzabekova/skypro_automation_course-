from selenium.webdriver import WebDriver


class ShopCartPage:
    """Корзина покупок."""

    CHECKOUT_BUTTON_LOCATOR = '[data-test="checkout"]'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def proceed_to_checkout(self) -> None:
        """Перейти к оформлению заказа."""
        btn = self.driver.find_element(By.CSS_SELECTOR, self.CHECKOUT_BUTTON_LOCATOR)
        btn.click()
        