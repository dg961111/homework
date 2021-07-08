import allure
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import DATA_DIR


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def scroll_locator(self, by, locator, num=3, reverse=False):
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:
                el = self.find(by, locator)
                self.driver.implicitly_wait(5)
                return el
            except NoSuchElementException:
                size = self.driver.get_window_size()
                width = size.get("width")
                height = size.get("height")

                x = width / 2
                start_y = height * 0.8
                end_y = height * 0.3
                if reverse:
                    start_y, end_y = end_y, start_y
                self.driver.swipe(x, start_y, x, end_y, 1000)
        raise NoSuchElementException("没有匹配的元素: ", by, locator)

    def scroll_locator_all(self, by, locator, end_by, end_locator, attribute, reverse=False):
        self.driver.implicitly_wait(1)
        result = []
        while True:
            try:
                els = self.finds(by, locator)
                for el in els:
                    try:
                        result.append(el.get_attribute(attribute))
                    except StaleElementReferenceException:
                        continue
                # 如果查询到了结束元素 则退出
                self.find(end_by, end_locator)
                self.driver.implicitly_wait(5)
                return list(set(result))
            except NoSuchElementException:
                size = self.driver.get_window_size()
                width = size.get("width")
                height = size.get("height")

                x = width / 2
                start_y = height * 0.8
                end_y = height * 0.3
                if reverse:
                    start_y, end_y = end_y, start_y
                self.driver.swipe(x, start_y, x, end_y, 1000)

    def find(self, by, locator):
        ele = self.driver.find_element(by, locator)
        return ele

    def finds(self, by, locator):
        elements = self.driver.find_elements(by, locator)
        return elements

    def find_and_click(self, by, locator):
        element = self.find(by, locator)
        element.click()

    def wait_for_click(self, by, locator, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator)))
        element.click()

    def find_and_send_keys(self, by, locator, keys):
        element = self.find(by, locator)
        element.send_keys(keys)

    def get_toast(self):
        el = self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
        return el

    def fail_picture(self, name):
        filename = DATA_DIR + rf'\error_picture\{name}.png'
        self.driver.get_screenshot_as_file(filename)
        allure.attach.file(filename, '失败用例截图:{filename}'.format(filename=name), allure.attachment_type.PNG)
