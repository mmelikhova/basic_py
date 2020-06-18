from selenium import webdriver
from fixture.session2 import SessionHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(120)
        self.session2 = SessionHelper(self)
        self.contact = ContactHelper(self)

    def return_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def open_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()