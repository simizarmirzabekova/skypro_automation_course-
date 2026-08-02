from selenium.webdriver import WebDriver


class CalculatorPage:
    """Класс описывает страницу Калькулятора."""

    URL = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'

    INPUT_DELAY_LOCATOR = '#delay'  # Поле задержки
    RESULT_LOCATOR = '.screen'      # Результат вычислений

    # Кнопки расположены в таблице, поэтому удобнее искать через xpath
    BUTTONS_XPATH_TEMPLATE = '//table[@id="keyboard"]//button[text()="{value}"]'
    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self) -> None:
        """Метод открывает сайт калькулятора."""
        self.driver.get(self.URL)

    def set_delay(self, seconds: int) -> None:
        """Устанавливает задержку перед отображением результата."""
        delay_field = self.driver.find_element('css selector', self.INPUT_DELAY_LOCATOR)
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_button(self, value: str) -> None:
        """
        Нажимает кнопку калькулятора по тексту на ней.
        
        :param value: Текст кнопки ('1', '+', '=' и т.д.)
        """
        button_xpath = self.BUTTONS_XPATH_TEMPLATE.format(value=value)
        button = self.driver.find_element('xpath', button_xpath)
        button.click()

    def get_result(self) -> float | None:
        """Возвращает результат вычисления или None, если он пустой."""
        result_el = self.driver.find_element('css selector', self.RESULT_LOCATOR)
        return float(result_el.text.strip()) if result_el.text else None
    