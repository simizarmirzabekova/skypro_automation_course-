from selenium import webdriver
from selenium.webdriver.common.by import By

def test_page_title():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")
    
    # Получаем первый заголовок (обычно это H1)
    title = driver.find_element(By.TAG_NAME, "h1").text
    # Проверяем, что слово присутствует (регистр неважен)
    assert "httpbin" in title.lower()
    driver.quit()
    