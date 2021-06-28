import allure
from faker import Faker
from util.read_data import ReadData


@allure.feature("企业微信添加联系人")
@allure.title("企业微信添加联系人")
def test_wework(get_driver):
    driver = get_driver
    # 先打开一次企业微信页面
    with allure.step("进入登录页面"):
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

    fake = Faker(locale="zh_CN")
    # 获取cookies信息,给当前打开的浏览器加上cookie信息
    with allure.step("获取cookie信息"):
        r = ReadData()
        for cookie in r.get_yaml_data("cookies.yml"):
            driver.add_cookie(cookie)

    # 进入企业微信首页
    with allure.step("进入首页"):
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    with allure.step("填写成员信息并保存"):
        name = fake.name()
        driver.find_element_by_id("menu_contacts").click()
        driver.find_element_by_link_text("添加成员").click()
        # 填写信息
        driver.find_element_by_id("username").send_keys(name)
        driver.find_element_by_id("memberAdd_english_name").send_keys(fake.user_name())
        driver.find_element_by_id("memberAdd_acctid").send_keys(fake.ean8())
        driver.find_element_by_id("memberAdd_phone").send_keys(fake.phone_number())
        driver.find_element_by_link_text("保存").click()

    # 获取所有成员进行断言
    with allure.step("断言是否添加成功"):
        users = driver.find_elements_by_css_selector('[id="member_list"] td:nth-child(2) span')
        assert name in [user.text for user in users]
