from selenium import webdriver
from selenium.webdriver.common.by import By

def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")

    # 1. Переходим по ссылке "HTML Forms"
    forms_link = driver.find_element(By.LINK_TEXT, "HTML Forms")
    forms_link.click()

    # 2. Проверяем, что попали на нужный адрес
    assert "/forms/post" in driver.current_url

    # 3. Возвращаемся назад
    driver.back()

    # 4. Проверяем, что вернулись на главную
    assert driver.current_url == "https://httpbin.org/"

    driver.quit()
    