from selenium.webdriver.common.by import By

from selenium_po0627.Pages.base_page import BasePage
from selenium_po0627.Pages.contact_page import ContactPage


class MainPage(BasePage):

    def __init__(self):
        super().__init__()
        self.contact_button = (By.ID, "menu_contacts")

    def go_to_concat(self):
        self.driver.find_element(*self.contact_button).click()
        return ContactPage()
