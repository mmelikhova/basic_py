# -*- coding: utf-8 -*-
# mmelikhova

import pytest
from model.contact import Contact
from fixture.contact_app import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        c = Contact(note="note", phone2="22", home_address="vit57", homepage="mln.ru",
                          middlename="Melikhov", lastname="Melikhov", nickname="mln_mln", firstname="Lesha",
                          company_address="VO 9th line", company="T-systems",
                          home_num="8898889", mob_num="5585558", work_num="558555", fax_num="4477",
                          mail1="mln@mln.com", mail2="mln1@mln.com", mail3="mln2@mln.com",
                          bday="2", bmonth="January", byear="1996",
                          aday="1", amonth="February", ayear="2003",
                          title_text="text")
        app.open_page()
        app.session2.login(login="admin", password="secret")
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
        app.session2.logout()

