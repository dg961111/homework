import allure
from faker import Faker


@allure.feature("企业微信手机端测试")
@allure.title("企业微信手机端测试")
class TestWorkWx:

    def setup(self):
        self.fake = Faker(locale="zh_CN")

    @allure.story("成功添加联系人")
    @allure.title('成功添加联系人')
    def test_add_contacts(self, mainPage):
        name = self.fake.name()
        result = mainPage.switch_to_contacts().add_member(name, self.fake.phone_number(), "男")
        assert "添加成功" == result
