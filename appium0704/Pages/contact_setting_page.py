import allure
from appium.webdriver.common.mobileby import MobileBy

from appium0704.Pages.base_page import BasePage
from appium0704.Pages.contact_edit_page import ContactEditPage


class ContactSettingPage(BasePage):
    _CONTACT_EDIT_BUTTON = (MobileBy.XPATH, '//*[@text="编辑成员"]')

    def switch_to_edit_page(self):
        with allure.step("切换至联系人编辑界面"):
            self.find_and_click(*self._CONTACT_EDIT_BUTTON)
            return ContactEditPage(self.driver)
