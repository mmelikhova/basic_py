from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        c=Contact(note="wwwfwefv", phone2="22", home_address="w3fr", homepage="wfw3",
                  middlename="FOR_EDIT", lastname="FOR_EDIT", nickname="FOR_EDIT", firstname="FOR_EDIT",
                  company_address="fwfww", company="Twefw",
                  home_num="233423", mob_num="33", work_num="dddg", fax_num="ee3",
                  mail1="342", mail2="odfgdgdg", mail3="dgdgdgd",
                  bday="2", bmonth="January", byear="1996",
                  aday="1", amonth="February", ayear="2003",
                  title_text="rw3rwefw4frwefw")
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
    old_contacts = app.contact.get_contact_list()
    c=Contact(note="note", phone2="66", home_address="Edited 15", homepage="Edited.ru",
              middlename="EDITED", lastname="EDITED", nickname="Edited", firstname="EDITED",
              company_address="VO Edited line", company="T-systems Edited",
              home_num="288869", mob_num="52555", work_num="5646546", fax_num="4477",
              mail1="Edited@mln.com", mail2="Edited@mln.com", mail3="Edited@mln.com",
              bday="2", bmonth="May", byear="1988",
              aday="1", amonth="July", ayear="2005",
              title_text="Edited text")
    app.contact.id = old_contacts[0].id
    app.contact.edit_contact()
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
    app.contact.submit_edit_contact()
    app.return_homepage()
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = [c.id, c.firstname, c.lastname]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



