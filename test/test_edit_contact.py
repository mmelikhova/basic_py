from model.contact import Contact


def test_edit_contact(app):
    c = Contact(note="note", phone2="66", home_address="Edited 15", homepage="Edited.ru",
                middlename="EDITED", lastname="EDITED", nickname="Edited", firstname="EDITED",
                company_address="VO Edited line", company="T-systems Edited",
                home_num="288869", mob_num="52555", work_num="5646546", fax_num="4477",
                mail1="Edited@mln.com", mail2="Edited@mln.com", mail3="Edited@mln.com",
                bday="2", bmonth="May", byear="1988",
                aday="1", amonth="July", ayear="2005",
                title_text="Edited text")
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


