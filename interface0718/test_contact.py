import allure
import pytest
from interface0718.api.contact import ContactApi
from util.read_data import ReadData

r = ReadData()
data = r.get_yaml_data("interface_contact")
add_data = data.get("add")
update_data = data.get("update")
delete_data = data.get("delete")
get_data = data.get("get")


@allure.title("企业微信通讯录api测试")
class TestContact:

    def setup_class(self):
        self.contact = ContactApi()
        setup_add = data.get("setup_add")
        for add in setup_add:
            self.contact.add(**add)

    def teardown_class(self):
        setup_add = data.get("setup_add")
        for add in setup_add:
            self.contact.delete(add.get("userid"))
        for user in [user[0].get("userid") for user in add_data.get("data")]:
            self.contact.delete(user)

    @allure.story("通讯录添加成员api")
    @pytest.mark.parametrize(add_data.get("args"), add_data.get("data"), ids=add_data.get("ids"))
    def test_add(self, value, expect):
        result = self.contact.add(**value)
        self.verify(expect, result.json())

    @allure.story("通讯录编辑成员成功")
    @pytest.mark.parametrize(update_data.get("args"), update_data.get("success").get("data"),
                             ids=update_data.get("success").get("ids"))
    def test_update_success(self, value, expect):
        result = self.contact.update(**value)
        self.verify(expect, result.json())
        user = self.contact.get(value.get("userid"))
        for k, v in value.items():
            assert user.json().get(k) == value.get(k)

    @allure.story("通讯录添加成员失败")
    @pytest.mark.parametrize(update_data.get("args"), update_data.get("fail").get("data"),
                             ids=update_data.get("fail").get("ids"))
    def test_update_fail(self, value, expect):
        result = self.contact.update(**value)
        self.verify(expect, result.json())

    @allure.story("通讯录删除成员api")
    @pytest.mark.parametrize(delete_data.get("args"), delete_data.get("data"), ids=delete_data.get("ids"))
    def test_delete(self, value, expect):
        result = self.contact.delete(**value)
        self.verify(expect, result.json())

    @allure.story("通讯录获取成员api")
    @pytest.mark.parametrize(get_data.get("args"), get_data.get("data"), ids=get_data.get("ids"))
    def test_get(self, value, expect):
        result = self.contact.get(**value)
        self.verify(expect, result.json())

    def verify(self, expect, reality):
        assert expect.get("code") == reality.get("errcode")
        assert expect.get("msg") in reality.get("errmsg")
