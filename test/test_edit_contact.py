from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        create_if_list_is_empty(app)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    c=Contact(note="note", phone2="66", home_address="Edited 15", homepage="Edited.ru",
              middlename="EDITED", lastname="EDITED", nickname="Edited", firstname="EDITED",
              company_address="VO Edited line", company="T-systems Edited",
              home_num="288869", mob_num="52555", work_num="5646546", fax_num="4477",
              mail1="Edited@mln.com", mail2="Edited@mln.com", mail3="Edited@mln.com",
              bday=str("2"), bmonth="May", byear="1988",
              aday=str("1"), amonth="may", ayear="2005",
              title_text="Edited text")
    app.contact.edit_contact_by_id(contact.id)
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
    old_contacts.remove(contact)
    old_contacts.append(c)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def create_if_list_is_empty(app):
    c=Contact(note="note", phone2="22", home_address="vit57", homepage="mln.ru",
              middlename="FORedit", lastname="Orbit", nickname="mln_mln", firstname="Jecka",
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


