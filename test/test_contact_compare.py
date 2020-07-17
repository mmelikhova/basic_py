import re
from random import randrange
from model.contact import Contact


def test_compare_contact_home_and_edit_pages(app):
    if app.contact.count() == 0:
        create_if_list_is_empty(app)
    index = randrange(app.contact.count())
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_editpage = app.contact.get_contact_info_from_editpage(index)
    assert contact_from_homepage.firstname == contact_from_editpage.firstname
    assert contact_from_homepage.lastname == contact_from_editpage.lastname
    assert contact_from_homepage.company_address == contact_from_editpage.company_address
    assert contact_from_homepage.all_mails_from_homepage == merge_mails_like_homepage(contact_from_editpage)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_homepage(contact_from_editpage)



def create_if_list_is_empty(app):
    c=Contact(note="note", phone2="22", home_address="vit57", homepage="mln.ru",
              middlename="FORDELETE", lastname="Orbit", nickname="mln_mln", firstname="Jecka",
              company_address="VO 9th line", company="T-systems",
              home_num="8898889", mob_num="5585558", work_num="558555", fax_num="4477",
              mail1="vas@mln.com", mail2="orbit@mln.com", mail3="mln2@mln.com",
              bday="2", bmonth="January", byear="1996",
              aday="1", amonth="February", ayear="2003",
              title_text="text")
    app.open_page()
    app.contact.add_new()
    app.contact.fill_name(c)
    app.contact.fill_title(c)
    app.contact.fill_company_info(c)
    app.contact.fill_phones(c)
    app.contact.fill_mails(c)
    app.contact.fill_homepage(c)
    app.contact.fill_bday(c)
    app.contact.fill_aday(c)
    app.contact.fill_homeaddress(c)
    app.contact.fill_homephone(c)
    app.contact.fill_note(c)
    app.contact.submit()
    app.return_homepage()


def merge_phones_like_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None, [contact.home_num, contact.mob_num,
                                                          contact.work_num, contact.phone2]))))


def merge_mails_like_homepage(contact):
     return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x), filter(lambda x: x is not None, [contact.mail1, contact.mail2,
                                                                              contact.mail3]))))


def clear(s):
    return re.sub("[() -+]", "", s)
