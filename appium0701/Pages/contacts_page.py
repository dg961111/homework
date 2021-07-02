import allure
from appium.webdriver.common.mobileby import MobileBy
from appium0701.Pages.base_page import BasePage


class ContactsPage(BasePage):
    _ADD_MEMBER_BUTTON = 'new UiSelector().text("添加成员")'
    _INPUT_ADD_MEMBER_BUTTON = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    _NAME_INPUT = (MobileBy.ID, "com.tencent.wework:id/au0")
    _PHONE_INPUT = (MobileBy.ID, "com.tencent.wework:id/eq7")
    _GENDER_BUTTON = (MobileBy.ID, "com.tencent.wework:id/av2")
    _SAVE_BUTTON = (MobileBy.ID, "com.tencent.wework:id/gur")

    def __init__(self, driver):
        super().__init__(driver)

    def add_member(self, name, phone, gender):
        with allure.step("滚动查找添加成员按钮"):
            self.scroll_locator(self._ADD_MEMBER_BUTTON).click()
        with allure.step("点击手动添加"):
            self.find_and_click(*self._INPUT_ADD_MEMBER_BUTTON)
        with allure.step("填入信息"):
            self.find_and_send_keys(*self._NAME_INPUT, name)
            self.find_and_send_keys(*self._PHONE_INPUT, phone)
            self.find_and_click(*self._GENDER_BUTTON)
            self.find_and_click(MobileBy.XPATH, f"//*[@resource-id='com.tencent.wework:id/b2x']/*[@text='{gender}']")
        with allure.step("保存并获取toast文本进行断言"):
            self.find_and_click(*self._SAVE_BUTTON)
            toast_el = self.get_toast()
        return toast_el.text
