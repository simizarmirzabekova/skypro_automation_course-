from selenium.webdriver.common.by import By

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, value: str):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear() # Очищаем поле перед вводом
        delay_input.send_keys(value)

    def press_button(self, text: str):
        # Ищем кнопку по тексту на ней
        button = self.driver.find_element(By.XPATH, f"//span[text()='{text}']")
        button.click()

    def get_result(self) -> str:
        result_element = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result_element.text
    