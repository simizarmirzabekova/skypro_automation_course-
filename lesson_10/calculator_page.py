from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        # Выносим локаторы в переменные (хороший тон)
        self.delay_locator = (By.CSS_SELECTOR, "#delay")
        self.result_locator = (By.CSS_SELECTOR, ".screen")

    def open(self):
        """
        Открывает страницу калькулятора.
        :return: None
        """
        self.driver.get(self.url)
    def set_delay(self, value: str):
 
     """
    Устанавливает задержку перед выполнением операций.
    :param value: str - значение задержки (например, "45")
    :return: None
    """
    # ваш старый код метода

    def press_button(self, text: str):
        # Ищем кнопку по тексту на ней
        button = self.driver.find_element(By.XPATH, f"//span[text()='{text}']")
        button.click()

    def get_result(self) -> str:
        # Ждем появления текста "15" в поле результата. 
        # Максимум ждем 45 секунд (как и указано в задании, но через умное ожидание, а не time.sleep).
        wait = WebDriverWait(self.driver, 47)
        wait.until(EC.text_to_be_present_in_element(self.result_locator, "15"))
        
        # Если текст "15" появился, возвращаем его
        return self.driver.find_element(*self.result_locator).text
    