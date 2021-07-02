import allure
import pytest
from selenium_po0627.Pages.base_page import BasePage
from util.read_data import ReadData

# 读取测试数据
r = ReadData()
data = r.get_yaml_data("wx_departments.yml")
success = data.get("success")
fail = data.get("fail")


@allure.feature("企业微信网页端测试")
@allure.title("企业微信网页端测试")
class TestAddDepartment:

    # 结束后清理掉测试生成的数据
    def teardown_class(self):
        main = BasePage()
        contact = main.switch_contacts_page()
        # 获取当前部门列表和要清理的部门列表
        departments = contact.get_departments()
        clear_names = [item[0] for item in success.get("data")]
        while True:
            # 获取所有非最后一级节点
            parents = [item.get("parent") for item in departments]
            diff_list = list(set(clear_names) - set(parents))
            # 清理最后一级节点
            for name in diff_list:
                contact.clear_departments(name)
            # 去掉已经清理掉的节点
            clear_names = list(set(clear_names) - set(diff_list))
            departments = [item for item in departments if item.get("name") not in diff_list]
            if not clear_names:
                break
        main.quit()

    @allure.story("成功添加部门")
    @allure.title('成功添加部门:')
    @pytest.mark.parametrize(argnames=success.get("args"), argvalues=success.get("data"), ids=success.get("ids"))
    def test_add_success(self, name, parent, mainPage):
        result = mainPage.switch_contacts_page().add_departments(name, parent).get_departments()
        with allure.step("断言添加的部门是否存在于部门列表中"):
            # 最后一条会报错，如果不刷新界面的话看不到刚加的部门
            assert {"name": name, "parent": parent} in result

    @allure.story("添加部门失败")
    @allure.title('添加部门失败:')
    @pytest.mark.parametrize(argnames=fail.get("args"), argvalues=fail.get("data"), ids=fail.get("ids"))
    def test_add_fail(self, name, parent, error_tip, mainPage):
        result = mainPage.switch_contacts_page().add_departments_fail(name, parent)
        with allure.step("断言错误提示是否与预期一致"):
            assert result == error_tip
