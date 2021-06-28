from selenium.webdriver.common.by import By

from selenium_po0627.Pages.base_page import BasePage
from selenium_po0627.Pages.contact_page import ContactPage


class AddMemberPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, "username")
        self.english_name_input = (By.ID, "memberAdd_english_name")
        self.acctid_input = (By.ID, "memberAdd_acctid")
        self.phone_input = (By.ID, "memberAdd_phone")

    def add_member(self, value):
        self.driver.find_element(*self.username_input).send_keys(value.get("name"))
        self.driver.find_element(*self.english_name_input).send_keys(value.get("english_name"))
        self.driver.find_element(*self.acctid_input).send_keys(value.get("acctid"))
        self.driver.find_element(*self.phone_input).send_keys(value.get("phone"))
        return ContactPage(self.driver)
