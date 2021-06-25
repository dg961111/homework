import os

import pytest
from selenium import webdriver


@pytest.fixture()
def get_driver():
    env = os.getenv("browser")
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('w3c', False)
    if env == "firefox":
        driver = webdriver.Firefox(options=opt)
    elif env == "chrome":
        driver = webdriver.Chrome(options=opt)
    elif env == "headless":
        driver = webdriver.PhantomJS()
    else:
        driver = webdriver.Chrome(options=opt)
    driver.maximize_window()

    # 全局隐式等待，
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
