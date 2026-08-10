import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Фикстура для Chrome (для теста калькулятора)

@pytest.fixture
def chrome_driver():
    options = ChromeOptions()
    # Добавим опции, чтобы браузер не мешал
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10) # Неявное ожидание
    yield driver
    driver.quit()

# Фикстура для Firefox (для теста магазина)


@pytest.fixture
def firefox_driver():
    options = FirefoxOptions()
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    