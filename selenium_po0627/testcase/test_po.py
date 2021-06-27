from faker import Faker
from selenium_po0627.Pages.main_page import MainPage


class TestAddMember:

    def setup(self):
        self.fake = Faker(locale="zh_CN")
        self.main = MainPage()

    def test_01(self):
        value = {
            "name": self.fake.name(),
            "english_name": self.fake.user_name(),
            "acctid": self.fake.ean8(),
            "phone": self.fake.phone_number()
        }
        result = self.main.go_to_concat().click_add_member().add_member(value).get_member()
        print(result)
        assert value.get("name") in result
