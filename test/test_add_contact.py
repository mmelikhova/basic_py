# -*- coding: utf-8 -*-
# mmelikhova

import pytest
from model.contact import Contact
from fixture.contact_app import Application


@pytest.fixture
def appr(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(appr):
        c = Contact(note="note", phone2="22", home_address="vit57", homepage="mln.ru",
                          middlename="Melikhov", lastname="Melikhov", nickname="mln_mln", firstname="Lesha",
                          company_address="VO 9th line", company="T-systems",
                          home_num="8898889", mob_num="5585558", work_num="558555", fax_num="4477",
                          mail1="mln@mln.com", mail2="mln1@mln.com", mail3="mln2@mln.com",
                          bday="2", bmonth="January", byear="1996",
                          aday="1", amonth="February", ayear="2003",
                          title_text="text")
        appr.open_page()
        appr.login(login="admin", password="secret")
        appr.add_new()
        appr.fill_name(c)
        appr.fill_title(c)
        appr.fill_company_info(c)
        appr.fill_phones(c)
        appr.fill_mails(c)
        appr.fill_homepage(c)
        appr.fill_bday(c)
        appr.fill_aday(c)
        appr.fill_homeaddress(c)
        appr.fill_homephone(c)
        appr.fill_note(c)
        appr.submit()
        appr.return_homepage()
        appr.logout()


