import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_adoption(parser):
    parser.addoption()




@pytest.fixture()
def setup():
    options = Options()
    options.page_load_strategy = 'eager'
    options.add_argument("--remote-allow-origins=*")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    try:
        driver.maximize_window()
    except Exception:
        pass
    
    yield driver
    
    try:
        driver.quit()
    except Exception:
        pass