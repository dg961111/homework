import allure
from appium.webdriver.common.mobileby import MobileBy
from appium0704.Pages.add_member_page import AddMemberPage
from appium0704.Pages.base_page import BasePage
from appium0704.Pages.user_page import UserPage


class ContactsPage(BasePage):
    _USERS = (MobileBy.XPATH,
              "//*[@resource-id='android:id/content']//android.widget.RelativeLayout/android.widget.FrameLayout[2]//android.widget.ListView/android.widget.RelativeLayout/android.widget.RelativeLayout//android.widget.TextView")
    _ADD_MEMBER_BUTTON = (MobileBy.XPATH, "//*[@text='添加成员']")
    _MY_CUSTOMER = (MobileBy.XPATH, "//*[@text='我的客户']")

    def switch_to_add_member(self):
        with allure.step("滚动查找进入添加成员页面"):
            self.scroll_locator(*self._ADD_MEMBER_BUTTON).click()
            return AddMemberPage(self.driver)

    def switch_to_user_page(self, username):
        with allure.step("切换至单个用户界面"):
            el = self.scroll_locator(MobileBy.XPATH, f"//*[@text='{username}']")
            el.click()
            return UserPage(self.driver)

    # 回到顶部
    def back_to_top(self):
        with allure.step("回到顶部"):
            self.scroll_locator(*self._MY_CUSTOMER, reverse=True)
            return self

    def get_all_user(self, reverse=False):
        with allure.step("获取所有联系人"):
            if reverse:
                end_el = self._MY_CUSTOMER
            else:
                end_el = self._ADD_MEMBER_BUTTON
            results = self.scroll_locator_all(*self._USERS, *end_el, attribute="text", reverse=reverse)
            # 返回之后不会得到最下面的添加客户
            try:
                results.remove("我的客户")
                results.remove("添加成员")
                results.remove("添加客户")
            except ValueError:
                pass
            return results
