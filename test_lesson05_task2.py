from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    # 1. Находим поле ввода и вводим свое имя
    name_input = driver.find_element(By.NAME, "custname")
    name_input.clear()
    name_input.send_keys("Симизар")

    # 2. Находим кнопку Submit и нажимаем
    submit_button = driver.find_element(By.XPATH, "//input[@value='Submit']")
    submit_button.click()

    # 3. Проверяем, что перешли на другую страницу
    assert driver.current_url != "https://httpbin.org/forms/post"

    driver.quit()
    