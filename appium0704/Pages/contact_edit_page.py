import allure
from appium.webdriver.common.mobileby import MobileBy

from appium0704.Pages.base_page import BasePage


class ContactEditPage(BasePage):
    _DELETE_CONTACT_BUTTON = (MobileBy.XPATH, '//*[@text="删除成员"]')
    _ALTER_ACCEPT_BUTTON = (MobileBy.XPATH, '//*[@text="确定"]')

    def delete_user(self):
        with allure.step("删除该联系人"):
            el = self.scroll_locator(*self._DELETE_CONTACT_BUTTON)
            el.click()
            self.find_and_click(*self._ALTER_ACCEPT_BUTTON)
        from appium0704.Pages.contacts_page import ContactsPage

        return ContactsPage(self.driver)
