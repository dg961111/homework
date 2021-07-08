from time import sleep

import allure
from appium.webdriver.common.mobileby import MobileBy
from appium0704.Pages.base_page import BasePage
from appium0704.Pages.member_info_page import MemberInfoPage


class AddMemberPage(BasePage):
    _INPUT_ADD_MEMBER_BUTTON = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    _BACK_BUTTON = (MobileBy.XPATH, "//*[@resource-id='android:id/content']/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")

    def switch_to_manual_page(self):
        with allure.step("进入手动添加页面"):
            self.find_and_click(*self._INPUT_ADD_MEMBER_BUTTON)
            return MemberInfoPage(self.driver)

    def back_to_contacts_page(self):
        with allure.step("返回通讯录页面"):
            self.wait_for_click(*self._BACK_BUTTON)
            from appium0704.Pages.contacts_page import ContactsPage

            return ContactsPage(self.driver)
