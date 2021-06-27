from selenium.webdriver.common.by import By

from selenium_po0627.Pages.base_page import BasePage


class ContactPage(BasePage):
    _ADD_USER_BUTTON = (By.LINK_TEXT, "添加成员")
    _ADD_IMG = (By.CSS_SELECTOR, ".member_colLeft_top_addBtnWrap js_create_dropdown")
    _OPEN_ADD_DEPARTMENT_BUTTON = (By.LINK_TEXT, "添加部门")
    _DEPARTMENT_NAME_INPUT = (By.CSS_SELECTOR, ".member_tag_dialog_inputDlg div:nth-child(1) > input")
    _DEPARTMENT_PARENT_LINK = (By.CSS_SELECTOR, ".qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list")
    _DEPARTMENTS_SELECT = (By.CSS_SELECTOR, '[class="jstree jstree-4 jstree-default"] a')
    _ADD_DEPARTMENT_BUTTON = (By.LINK_TEXT, "确定")

    def __init__(self):
        super().__init__()

    def click_add_member(self):
        from selenium_po0627.Pages.add_member_page import AddMemberPage
        self.driver.find_element(*self._ADD_USER_BUTTON).click()
        return AddMemberPage()

    def get_member(self):
        users = self.driver.find_elements_by_css_selector('[id="member_list"] td:nth-child(2) span')
        return users

    def get_departments(self):
        all_departments = {}

        def departments():
            elements = self.finds(By.CSS_SELECTOR, '[class="jstree jstree-3 jstree-default"]>ul>li')