from time import sleep
import allure
from selenium.webdriver.common.by import By
from selenium_po0627.Pages.base_page import BasePage


class ContactPage(BasePage):
    _ADD_USER_BUTTON = (By.LINK_TEXT, "添加成员")
    _ADD_IMG = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    _OPEN_ADD_DEPARTMENT_BUTTON = (By.LINK_TEXT, "添加部门")
    _DEPARTMENT_NAME_INPUT = (By.CSS_SELECTOR, ".member_tag_dialog_inputDlg div:nth-child(1) > input")
    _DEPARTMENT_PARENT_LINK = (By.CSS_SELECTOR, ".member_tag_dialog_inputDlg div:nth-child(3) > a")
    _ADD_DEPARTMENT_BUTTON = (By.LINK_TEXT, "确定")
    _TIPS = (By.CSS_SELECTOR, '#js_tips')

    def __init__(self, driver=None):
        super().__init__(driver)

    def __open_all_expend(self, where=None):
        # 展开所有下拉 where代表哪个标签之下
        locator = 'li[class*="jstree-closed"]>i'
        if where:
            locator = where + ' li[class*="jstree-closed"]>i'
        while True:
            sleep(1)
            expend_elements = self.finds(By.CSS_SELECTOR, locator)
            if not expend_elements:
                return
            for ele in expend_elements:
                ele.click()

    def click_add_member(self):
        from selenium_po0627.Pages.add_member_page import AddMemberPage
        self.driver.find_element(*self._ADD_USER_BUTTON).click()
        return AddMemberPage(self.driver)

    def get_member(self):
        users = self.driver.find_elements_by_css_selector('[id="member_list"] td:nth-child(2) span')
        self.driver.find_element_by_link_text()

        return users

    def add_departments(self, name, parent):
        # 打开添加部门弹窗
        with allure.step("打开添加部门弹窗"):
            self.find_and_click(*self._ADD_IMG)
            self.find_and_click(*self._OPEN_ADD_DEPARTMENT_BUTTON)
        # 输入内容
        with allure.step("输入信息"):
            self.find_and_send_keys(*self._DEPARTMENT_NAME_INPUT, name)
            self.find_and_click(*self._DEPARTMENT_PARENT_LINK)
            # 展开inputDlg下的所有列表
            self.__open_all_expend('.inputDlg_item')
            self.find_and_click(By.XPATH, f'//*[@class="inputDlg_item"]//a[text()="{parent}"]')
        # 点击确认
        with allure.step("点击确认添加"):
            self.find_and_click(*self._ADD_DEPARTMENT_BUTTON)
        return self

    def add_departments_fail(self, name, parent=''):
        # 打开添加部门弹窗
        with allure.step("打开添加部门弹窗"):
            self.find_and_click(*self._ADD_IMG)
            self.find_and_click(*self._OPEN_ADD_DEPARTMENT_BUTTON)
        # 输入内容
        with allure.step("输入信息"):
            self.find_and_send_keys(*self._DEPARTMENT_NAME_INPUT, name)
            if parent:
                self.find_and_click(*self._DEPARTMENT_PARENT_LINK)
                # 展开inputDlg下的所有列表
                self.__open_all_expend('.inputDlg_item')
                self.find_and_click(By.XPATH, f'//*[@class="inputDlg_item"]//a[text()="{parent}"]')
        # 点击确认
        with allure.step("点击确认添加"):
            self.find_and_click(*self._ADD_DEPARTMENT_BUTTON)
        # 断言提示框
        with allure.step("获取错误提示信息"):
            tip = self.find(*self._TIPS)
        return tip.text

    def get_departments(self):
        departments_data = []

        # 递归搜索所有的部门
        def departments(children, parent):
            for el in children:
                departments_data.append({"name": el.text, "parent": parent})
                el_id = el.get_attribute("id")
                children_element = self.finds(By.CSS_SELECTOR, f'[id="{el_id}"]+ul>li>a')
                if children_element:
                    departments(children_element, el.text)
        self.__open_all_expend()

        # 添加第一级部门 以及搜索所有部门
        with allure.step("获取所有的部门"):
            first_department = self.find(By.CSS_SELECTOR, '[aria-level="1"]>a')
            first_department_id = first_department.get_attribute("id")
            departments_data.append({"name": first_department.text, "parent": -1})
            children_ele = self.finds(By.CSS_SELECTOR, f'[id="{first_department_id}"]+ul>li>a')
            if children_ele:
                departments(children_ele, first_department.text)
        return departments_data

    # 清除测试数据产生的部门
    def clear_departments(self, name):
        with allure.step("清理添加的部门"):
            self.wait_for_click(By.LINK_TEXT, name)
            sleep(1)
            self.wait_for_click(By.CSS_SELECTOR, 'a[class*="jstree-clicked"]>span')
            self.wait_for_click(By.LINK_TEXT, "删除")
            self.wait_for_click(By.LINK_TEXT, "确定")
            sleep(1)
