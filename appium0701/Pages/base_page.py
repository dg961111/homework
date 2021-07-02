import allure
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from settings import DATA_DIR


class BasePage:
    _CONTACTS_BUTTON = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/dqn" and @text="通讯录"]')

    def __init__(self, driver: WebDriver = None):
        if driver:
            self.driver = driver
        else:
            desired_caps = {
                "platformName": "android",
                "deviceName": "emulator-5554",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": "true",
                'skipServerInstallation': True,
                'skipDeviceInitialization': True,
            }
            self.driver = webdriver.Remote("127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(5)

    def switch_to_contacts(self):
        with allure.step("切换至联系人界面"):
            self.find_and_click(*self._CONTACTS_BUTTON)
        from appium0701.Pages.contacts_page import ContactsPage

        return ContactsPage(self.driver)

    def scroll_locator(self, ui_automator_locator):
        el = self.driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView({ui_automator_locator}.instance(0))')
        return el

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