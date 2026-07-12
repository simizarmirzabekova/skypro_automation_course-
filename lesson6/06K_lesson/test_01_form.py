import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.skipif(
    not pytest.config.getoption("--browser") in ["edge", "safari"],
    reason="Test requires Edge or Safari"
)
def test_form():
    """Автотест формы"""

    # Выбор браузера зависит от аргумента командной строки
    browser_name = pytest.config.getoption("--browser")
    if browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError("Unsupported browser for this test")

    try:
        wait = WebDriverWait(driver, 10)

        # 1. Открываем страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # 2. Заполняем форму
        first_name_field = driver.find_element(By.CSS_SELECTOR, "#first-name")
        last_name_field = driver.find_element(By.CSS_SELECTOR, "#last-name")
        address_field = driver.find_element(By.CSS_SELECTOR, "#address")
        email_field = driver.find_element(By.CSS_SELECTOR, "#email")
        phone_field = driver.find_element(By.CSS_SELECTOR, "#phone")
        city_field = driver.find_element(By.CSS_SELECTOR, "#city")
        country_field = driver.find_element(By.CSS_SELECTOR, "#country")
        job_title_field = driver.find_element(By.CSS_SELECTOR, "#job-title")
        company_field = driver.find_element(By.CSS_SELECTOR, "#company")

        submit_button = driver.find_element(By.CSS_SELECTOR, "#submit")

        # Отправляем данные
        first_name_field.send_keys("Иван")
        last_name_field.send_keys("Петров")
        address_field.send_keys("Ленина, 55-3")
        email_field.send_keys("test@skypro.com")
        phone_field.send_keys("+7985899998787")
        # Zip code оставляем пустым
        city_field.send_keys("Москва")
        country_field.send_keys("Россия")
        job_title_field.send_keys("QA")
        company_field.send_keys("SkyPro")

        # Ждём, пока кнопка станет кликабельной (иногда форма подгружается медленно)
        wait.until(EC.element_to_be_clickable(submit_button))
        submit_button.click()

        # 3. Проверки
        # Ожидание того, что страница обновилась после отправки
        wait.until(EC.url_changes(driver.current_url))

        # Проверяем красный фон поля ZIP Code
        zip_code_field = driver.find_element(By.CSS_SELECTOR, "#zip-code")
        assert (
            zip_code_field.value_of_css_property("background-color").lower() 
            == "rgba(255, 0, 0, 1)"  # Красный цвет
        ), f"Поле ZIP не красное: {zip_code_field.value_of_css_property('background-color')}"

        # Проверяем зелёный фон остальных полей
        fields_to_check = [
            first_name_field,
            last_name_field,
            address_field,
            email_field,
            phone_field,
            city_field,
            country_field,
            job_title_field,
            company_field,
        ]

        for field in fields_to_check:
            color = field.value_of_css_property("background-color").lower()
            assert color == "rgba(0, 255, 0, 1)", f"Поле {field.tag_name} не зеленое: {color}"

    finally:
        driver.quit()
        