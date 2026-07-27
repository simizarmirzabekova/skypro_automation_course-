from selenium import webdriver
from selenium.webdriver.common.by import By

def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    # 1. Находим ВСЕ ссылки на странице
    all_links = driver.find_elements(By.TAG_NAME, "a")

    # 2. Проверяем, что их именно 9
    assert len(all_links) == 9

    # 3. Проверяем, что каждая ссылка отображается
    for link in all_links:
        assert link.is_displayed()

    # 4. Проверяем первую ссылку
    first_link_text = all_links[0].text
    assert "1" in first_link_text

    driver.quit()
    