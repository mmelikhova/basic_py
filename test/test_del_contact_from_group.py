from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

orm = ORMFixture(host= '127.0.0.1', name = 'addressbook', user = 'root', password = '')


def test_del_contact_from_group(app, db):
    #precondition if lists are empty
    if len(db.get_contact_list()) == 0:
        create_if_list_is_empty(app)
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="xxx"))
    contact=random.choice(db.get_contact_list())
    group=random.choice(db.get_group_list())
    contacts_in_group=orm.get_contacts_in_group(Group(id=group.id))
    if contact not in contacts_in_group:
        app.contact.add_contact_to_group_by_ids(contact, group)
        app.homepage()
    #step  #deletion
    app.contact.delete_contact_from_group(contact, group)
    #validation
    contacts_not_in_group = orm.get_contacts_not_in_group(Group(id=group.id))
    if contact not in contacts_not_in_group:
        raise ValueError("ERROR: contact %s found in group %s" % contact % group)



def create_if_list_is_empty(app):
    c=Contact(note="note", phone2="22", home_address="vit57", homepage="mln.ru",
              middlename="To_Group", lastname="To_Group", nickname="mln_mln", firstname="Jecka",
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