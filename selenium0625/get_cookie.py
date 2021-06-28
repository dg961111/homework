import yaml
from selenium import webdriver


def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    cookies = driver.get_cookies()
    driver.find_element_by_id("menu_contacts").click()
    with open("../data/cookies.yml", "w") as f:
        yaml.safe_dump(cookies, f)
    print(cookies)

