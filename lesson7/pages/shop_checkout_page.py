from selenium.webdriver import WebDriver


class ShopCheckoutPage:
    """Страница Checkout: Your Information."""

    FIRST_NAME_FIELD_LOCATOR = '[data-test="firstName"]'
    LAST_NAME_FIELD_LOCATOR = '[data-test="lastName"]'
    POSTAL_CODE_FIELD_LOCATOR = '[data-test="postalCode"]'

    CONTINUE_BUTTON_LOCATOR = '[data-test="continue"]'

    TOTAL_PRICE_LOCATOR = '.summary_total_label'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def fill_form(
            self,
            first_name: str,
            last_name: str,
            postal_code: str
    ) -> None:
        """Заполняет форму доставки."""
        fn_field = self.driver.find_element(By.CSS_SELECTOR, self.FIRST_NAME_FIELD_LOCATOR)
        ln_field = self.driver.find_element(By.CSS_SELECTOR, self.LAST_NAME_FIELD_LOCATOR)
        pc_field = self.driver.find_element(By.CSS_SELECTOR, self.POSTAL_CODE_FIELD_LOCATOR)

        fn_field.send_keys(first_name)
        ln_field.send_keys(last_name)
        pc_field.send_keys(postal_code)

    def continue_to_overview(self) -> None:
        """Жмёт кнопку Continue, переходит к итоговому экрану."""
        btn = self.driver.find_element(By.CSS_SELECTOR, self.CONTINUE_BUTTON_LOCATOR)
        btn.click()

    def get_total_price(self) -> float:
        """Получает итоговую сумму заказа."""
        total_text = self.driver.find_element(By.CSS_SELECTOR, self.TOTAL_PRICE_LOCATOR).text
        price_str = total_text.split(':')[1].strip().replace('$', '')
        return float(price_str)
    