import allure
from appium.webdriver.common.mobileby import MobileBy

from appium0704.Pages.base_page import BasePage
from appium0704.Pages.contact_setting_page import ContactSettingPage


class UserPage(BasePage):
    _SETTING_USER_BUTTON = (MobileBy.XPATH,
                            '//*[@resource-id="android:id/content"]//android.widget.RelativeLayout/android.widget.LinearLayout[2]//android.widget.TextView')

    def switch_to_setting_user_page(self):
        with allure.step("切换至联系人设置页面"):
            self.wait_for_click(*self._SETTING_USER_BUTTON)
            return ContactSettingPage(self.driver)
