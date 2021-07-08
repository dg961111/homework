import allure
from appium.webdriver.common.mobileby import MobileBy
from appium0704.Pages.base_page import BasePage


class MemberInfoPage(BasePage):
    _NAME_INPUT = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText")
    _PHONE_INPUT = (MobileBy.XPATH, "//*[contains(@text, '手机')]/..//android.widget.EditText")
    _SAVE_BUTTON = (MobileBy.XPATH, "//*[@text='保存']")

    def input_member_info(self, name, phone):
        with allure.step("填入信息"):
            self.find_and_send_keys(*self._NAME_INPUT, name)
            self.find_and_send_keys(*self._PHONE_INPUT, phone)
        with allure.step("保存"):
            self.find_and_click(*self._SAVE_BUTTON)
        from appium0704.Pages.add_member_page import AddMemberPage

        return AddMemberPage(self.driver)
