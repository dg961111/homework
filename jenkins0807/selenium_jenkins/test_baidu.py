from time import sleep

import allure
from selenium import webdriver


@allure.feature("百度关键词测试")
class TestBaidu:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    @allure.story("搜索关键词: sanlu")
    def test_01(self):
        key_word = "sanlu"
        self.search_keyword(key_word)

    @allure.story("搜索关键词: 阿里巴巴")
    def test_02(self):
        key_word = "阿里巴巴"
        self.search_keyword(key_word)

    def search_keyword(self, key_word):
        with allure.step("输入关键字并搜索"):
            self.driver.find_element_by_id("kw").send_keys(key_word)
            self.driver.find_element_by_id("su").click()
        sleep(2)

        with allure.step("断言搜索关键字是否存在标题上"):
            assert key_word in self.driver.title

    def teardown(self):
        self.driver.quit()
