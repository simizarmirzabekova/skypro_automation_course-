import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.skipif(
    pytest.config.getoption("--browser") != "chrome",
    reason="Test requires Google Chrome"
)
def test_calculator():
    """Автотест калькулятора"""

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)  # Долго ждём результат

    try:
        # 1. Открываем страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # 2. Устанавливаем задержку
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # 3. Нажимаем кнопки
        buttons = {
            "7": driver.find_element(By.XPATH, "//span[text()='7']"),
            "+": driver.find_element(By.XPATH, "//span[text()='+']"),
            "8": driver.find_element(By.XPATH, "//span[text()='8']"),
            "=": driver.find_element(By.XPATH, "//span[text()='=']"),
        }

        for button_text in ["7", "+", "8", "="]:
            buttons[button_text].click()

        # 4. Ждем результата
        result_locator = (By.ID, "result")
 lesson6K
        wait.until(EC.text_to_be_present_in_element(result_locator, "15"))
        result = driver.find_element(*result_locator).text
=======
        # Ждем, пока текст изменится с дефолтного "0" на другой
        wait.until(EC.text_to_be_present_in_element_value(result_locator, "15"))

 main
        # 5. Проверка
        result = driver.find_element(*result_locator).get_attribute("value")
        assert result == "15", f"Результат неверен: {result}"

    finally:
        driver.quit()
        