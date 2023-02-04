from time import sleep

import pytest
from time import sleep
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture

def browser():
    #before tests - ce se face inainte  de fiecare test
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # maximaze window
    driver.maximize_window()
    yield driver
    #return driver -  tabul pe care noi lucram

    #after test -  ce vrem sa facem dupa fiecare test
    driver.quit