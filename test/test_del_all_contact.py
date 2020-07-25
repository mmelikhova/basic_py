from model.contact import Contact


def test_delete_all_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        create_if_list_is_empty(app)
    old_contacts=db.get_contact_list()
    app.contact.delete_all_contact()
    app.homepage()
    new_contacts=db.get_contact_list()
    assert len(old_contacts) - len(new_contacts) == len(old_contacts)
    old_contacts.clear()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

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