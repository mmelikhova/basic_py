# -*- coding: utf-8 -*-
# mmelikhova


from model.contact import Contact


def test_add_contact(app):
    c=Contact(note="note", phone2="22", home_address="vit57", homepage="mln.ru",
              middlename="fggjjk", lastname="ttt", nickname="mln_mln", firstname="gfgdg",
              company_address="VO 9th line", company="T-systems",
              home_num="8898889", mob_num="5585558", work_num="558555", fax_num="4477",
              mail1="vas@mln.com", mail2="orbit@mln.com", mail3="mln2@mln.com",
              bday="2", bmonth="January", byear="1996",
              aday="1", amonth="February", ayear="2003",
              title_text="text")
    old_contacts=app.contact.get_contact_list()
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
    new_contacts=app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(c.id,  c.lastname, c.firstname,)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




