from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from util.read_data import ReadData


class BasePage:
    _INDEX_BUTTON = (By.ID, "menu_index")
    _CONTACTS_BUTTON = (By.ID, "menu_contacts")
    _APPS_BUTTON = (By.ID, "menu_apps")

    def __init__(self, driver: WebDriver = None):
        if driver:
            self.driver = driver
        else:
            opt = webdriver.ChromeOptions()
            opt.add_experimental_option('w3c', False)
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(5)
            # 先打开一次企业微信页面
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

            # 获取cookies信息,给当前打开的浏览器加上cookie信息
            r = ReadData()
            for cookie in r.get_yaml_data("cookies.yaml"):
                self.driver.add_cookie(cookie)

            # 进入企业微信首页
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def quit(self):
        self.driver.quit()

    def find(self, by, locator):
        ele = self.driver.find_element(by, locator)
        return ele

    def finds(self, by, locator):
        elements = self.driver.find_elements(by, locator)
        return elements

    def find_and_click(self, by, locator):
        element = self.find(by, locator)
        element.click()

    def switch_index_page(self):
        self.find_and_click(*self._INDEX_BUTTON)

    def switch_contacts_page(self):
        self.find_and_click(*self._CONTACTS_BUTTON)

    def switch_apps_page(self):
        self.find_and_click(*self._APPS_BUTTON)

