import allure
from faker import Faker


@allure.title("企业微信手机端测试")
class TestWorkWx:
    def setup_class(self):
        self.fake = Faker(locale="zh_CN")
        self.name = self.fake.name()
        self.phone = self.fake.phone_number()

    @allure.title('成功添加联系人')
    def test_add_contacts(self, app):
        users = app.switch_to_contacts().\
            switch_to_add_member().\
            switch_to_manual_page().\
            input_member_info(self.name, self.phone).\
            back_to_contacts_page().\
            back_to_top().\
            get_all_user()
        with allure.step("断言用户是否存在于联系人列表中"):
            assert self.name in users

    @allure.title('成功删除联系人')
    def test_delete_contacts(self, app):
        users = app.switch_to_contacts().\
            switch_to_user_page(self.name).\
            switch_to_setting_user_page().\
            switch_to_edit_page().\
            delete_user().\
            back_to_top().\
            get_all_user()
        with allure.step("断言用户是否已经不存在于联系人列表中"):
            assert self.name not in users
