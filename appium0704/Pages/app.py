from appium import webdriver
from appium0704.Pages.base_page import BasePage
from appium0704.Pages.main_page import MainPage


class App(BasePage):

    def start(self):
        if self.driver:
            self.driver.launch_app()
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
        return self

    def restart(self):
        self.driver.launch_app()
        return self

    def quit(self):
        self.driver.quit()

    def switch_to_base(self):
        return MainPage(self.driver)
