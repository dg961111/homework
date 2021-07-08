import allure
from appium.webdriver.common.mobileby import MobileBy

from appium0704.Pages.base_page import BasePage


class MainPage(BasePage):
    _CONTACTS_BUTTON = (MobileBy.XPATH, '//*[@text="通讯录"]')

    def switch_to_contacts(self):
        with allure.step("切换至联系人界面"):
            self.find_and_click(*self._CONTACTS_BUTTON)
        from appium0704.Pages.contacts_page import ContactsPage

        return ContactsPage(self.driver)

