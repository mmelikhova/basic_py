# -*- coding: utf-8 -*-
# mmelikhova

import pytest
from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols=string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


month_list=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
            'November', 'December']


testdata=[Contact(note="", phone2="", home_address="", homepage="",
                  middlename="", lastname="", nickname="", firstname="",
                  company_address="", company="",
                  home_num="", mob_num="", work_num="", fax_num="",
                  mail1="", mail2="", mail3="",
                  bday="", bmonth="-", byear="",
                  aday="", amonth="-", ayear="",
                  title_text="")] + [Contact(note=random_string("note", 20),
                                             phone2=random_string("ph2", 10),
                                             home_address=random_string("homeadd", 20),
                                             homepage=random_string("homepage", 20),
                                             middlename=random_string("midn", 25), lastname=random_string("lastn", 25),
                                             nickname=random_string("nick", 25), firstname=random_string("firstn", 25),
                                             company_address=random_string("compadd", 35),
                                             company=random_string("compname", 20),
                                             home_num=random_string("homeph", 10), mob_num=random_string("mobph", 10),
                                             work_num=random_string("workph", 10), fax_num=random_string("fax", 10),
                                             mail1=random_string("1mail", 20), mail2=random_string("2mail", 20),
                                             mail3=random_string("3mail", 20),
                                             bday=str(random.randrange(0, 31, 1)), bmonth=random.choice(month_list),
                                             byear=str(random.randrange(1900, 2020, 1)),
                                             aday=str(random.randrange(0, 31, 1)), amonth=random.choice(month_list),
                                             ayear=str(random.randrange(1900, 2020, 1)),
                                             title_text=random_string("title", 10))
                                     for i in range(2)
                                     ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts=app.contact.get_contact_list()
    app.contact.add_new()
    app.contact.fill_name(contact)
    app.contact.fill_title(contact)
    app.contact.fill_company_info(contact)
    app.contact.fill_phones(contact)
    app.contact.fill_mails(contact)
    app.contact.fill_homepage(contact)
    app.contact.fill_bday(contact)
    app.contact.fill_aday(contact)
    app.contact.fill_homeaddress(contact)
    app.contact.fill_homephone(contact)
    app.contact.fill_note(contact)
    app.contact.submit()
    app.return_homepage()
    new_contacts=app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
