from selenium.webdriver import WebDriver


class LoginPage:
    """Страница входа на saucedemo.com"""

    URL = 'https://www.saucedemo.com/'

    LOGIN_FIELD_LOCATOR = '[data-test="username"]'
    PASSWORD_FIELD_LOCATOR = '[data-test="password"]'
    LOGIN_BUTTON_LOCATOR = '[data-test="login-button"]'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self) -> None:
        self.driver.get(self.URL)

    def enter_credentials(self, username: str, password: str) -> None:
        """Заполняет поля логина и пароля."""
        user_field = self.driver.find_element(By.CSS_SELECTOR, self.LOGIN_FIELD_LOCATOR)
        pass_field = self.driver.find_element(By.CSS_SELECTOR, self.PASSWORD_FIELD_LOCATOR)
        user_field.send_keys(username)
        pass_field.send_keys(password)

    def submit_login(self) -> None:
        """Нажимает кнопку Входа."""
        btn = self.driver.find_element(By.CSS_SELECTOR, self.LOGIN_BUTTON_LOCATOR)
        btn.click()
        