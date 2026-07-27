from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():

    driver = webdriver.Edge()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # заполнить поля значениями ->
    form_data = {
        'first-name': 'Иван',
        'last-name': 'Петров',
        'address': 'Ленина, 55-3',
        'e-mail': 'test@skypro.com',
        'phone': '+7985899998787',
        'city': 'Москва',
        'country': 'Россия',
        'job-position': 'QA',
        'company': 'SkyPro'
    }

    # Заполняем все поля через цикл
    for field_name, value in form_data.items():
        field = driver.find_element(By.CSS_SELECTOR, f'[name="{field_name}"]')
        field.send_keys(value)
        print(f"✓ Заполнено поле '{field_name}' значением '{value}'")

    # найти, не выполняя никаких действий
    driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]')

    # нажать submit
    driver.find_element(By.CSS_SELECTOR, 'button').click()

    # ждем .alert (принятие формой данных, явное ожидание)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))

    element = driver.find_element(
        By.CSS_SELECTOR, '#zip-code').get_attribute('class')

    assert "alert-danger" in element, f'Пришел {element}'

    elements = [
        'first-name',
        'last-name',
        'address',
        'e-mail',
        'phone',
        'city',
        'country',
        'job-position',
        'company'
        ]

    for e in elements:
        element = driver.find_element(By.CSS_SELECTOR, f'#{e}')
        class_attr = element.get_attribute('class') or ''
        assert "alert-success" in class_attr

    driver.quit()
