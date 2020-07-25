from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()
        self.contact_cache=None

    def fill_note(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.note)
        self.contact_cache=None

    def fill_homephone(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        self.contact_cache=None

    def fill_homeaddress(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.home_address)
        self.contact_cache=None

    def fill_aday(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_value(contact.aday)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_value(contact.amonth)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        self.contact_cache=None

    def fill_bday(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_value(contact.bday)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_value(contact.bmonth)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        self.contact_cache=None

    def fill_homepage(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        self.contact_cache=None

    def fill_mails(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.mail1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.mail2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.mail3)
        self.contact_cache=None

    def fill_phones(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_num)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mob_num)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_num)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_num)
        self.contact_cache=None

    def fill_company_info(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/label[7]").click()
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.company_address)
        self.contact_cache=None

    def fill_title(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title_text)
        self.contact_cache=None

    def fill_name(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        self.contact_cache=None

    def add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.contact_cache=None

    def edit_contact_by_id(self, id):
        wd = self.app.wd
        # click on edit button(pencil)
        wd.find_element_by_css_selector("a[href$='edit.php?id="+str(id)+"']").click()
        self.contact_cache=None

    def edit_contact(self):
        wd=self.app.wd
        # click on edit button(pencil)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.contact_cache=None

    def submit_edit_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.contact_cache=None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache=None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache=None

    def select_contact_by_index(self, index):
        wd=self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd=self.app.wd
        wd.find_element_by_id(str(id)).click()

    def delete_all_contact(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd=self.app.wd
            self.app.open_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name('entry'):
                sector = row.find_elements_by_tag_name("td")
                firstname = sector[1].text
                lastname = sector[2].text
                id = sector[0].find_element_by_name("selected[]").get_attribute("id")
                company_address = sector[3].text
                all_mails = sector[4].text
                all_phones = sector[5].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                  company_address=company_address,
                                                  all_mails_from_homepage= all_mails,
                                                  all_phones_from_homepage = all_phones))
            return list(self.contact_cache)

    def view_contact_by_id(self, id):
        wd = self.app.wd
        # click on edit button(pencil)
        wd.find_element_by_css_selector("a[href$='view.php?id="+str(id)+"']").click()
        self.contact_cache=None

    def open_contact_to_edit_by_index(self, index):
        wd=self.app.wd
        self.app.open_page()
        row = wd.find_elements_by_name('entry')[index]
        sector = row.find_elements_by_tag_name("td")[7]
        sector.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd=self.app.wd
        self.app.open_page()
        row=wd.find_elements_by_name('entry')[index]
        sector=row.find_elements_by_tag_name("td")[6]
        sector.find_element_by_tag_name("a").click()

    def get_contact_info_from_editpage(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        company_address = wd.find_element_by_name("address").text
        mail1 = wd.find_element_by_name("email").get_attribute("value")
        mail2=wd.find_element_by_name("email2").get_attribute("value")
        mail3=wd.find_element_by_name("email3").get_attribute("value")
        home_num = wd.find_element_by_name("home").get_attribute("value")
        mob_num=wd.find_element_by_name("mobile").get_attribute("value")
        work_num=wd.find_element_by_name("work").get_attribute("value")
        phone2=wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       company_address = company_address,
                       mail1=mail1, mail2=mail2, mail3=mail3,
                       home_num=home_num,
                       mob_num=mob_num, work_num=work_num, phone2=phone2)

    def get_contact_info_from_viewpage(self, index):
        wd=self.app.wd
        wd.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_num = re.search("H: (.*)", text).group(1)
        mob_num=re.search("M: (.*)", text).group(1)
        work_num=re.search("W: (.*)", text).group(1)
        phone2=re.search("P: (.*)", text).group(1)
        return Contact(home_num=home_num,
                       mob_num=mob_num, work_num=work_num, phone2=phone2)

