from time import sleep

from selenium import webdriver


class TestBaidu:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def test_01(self):
        key_word = "sanlu"
        self.search_keyword(key_word)

    def test_02(self):
        key_word = "阿里巴巴"
        self.search_keyword(key_word)

    def search_keyword(self, key_word):
        self.driver.find_element_by_id("kw").send_keys(key_word)
        self.driver.find_element_by_id("su").click()
        sleep(2)

        assert key_word in self.driver.title

    def teardown(self):
        self.driver.quit()
