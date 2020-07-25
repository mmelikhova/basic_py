import re
from model.contact import Contact


def test_compare_contacts_home_and_db(app, db):
    if len(db.get_contact_list()) == 0:
        create_if_list_is_empty(app)
    contacts_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_from_db) == len(contacts_from_homepage)
    for i in range(len(contacts_from_db)):
        contacts_from_db[i].all_phones_from_db = merge_phones_like_homepage(contacts_from_db[i])
        contacts_from_db[i].all_mails_from_db = merge_mails_like_homepage(contacts_from_db[i])
        assert contacts_from_db[i].firstname == contacts_from_homepage[i].firstname
        assert contacts_from_db[i].lastname == contacts_from_homepage[i].lastname
        assert contacts_from_db[i].company_address == contacts_from_homepage[i].company_address
        assert contacts_from_db[i].all_phones_from_db == contacts_from_homepage[i].all_phones_from_homepage
        assert contacts_from_db[i].all_mails_from_db == contacts_from_homepage[i].all_mails_from_homepage


def create_if_list_is_empty(app):
    c=Contact(note="note", phone2="22", home_address="vit57", homepage="mln.ru",
              middlename="FORDELETE", lastname="Orbit", nickname="mln_mln", firstname="Jecka",
              company_address="VO 9th line", company="T-systems",
              home_num="8898889", mob_num="5585558", work_num="558555", fax_num="4477",
              mail1="vas@mln.com", mail2="orbit@mln.com", mail3="mln2@mln.com",
              bday="2", bmonth="January", byear="1996",
              aday="1", amonth="february", ayear="2003",
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
