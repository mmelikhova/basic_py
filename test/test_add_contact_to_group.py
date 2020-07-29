from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

orm = ORMFixture(host= '127.0.0.1', name = 'addressbook', user = 'root', password = '')


def test_add_contact_to_group(app, db):
    if len(orm.get_contacts_not_in_any_group()) == 0: #проверка: если список контактов без группы пуст - создать
        create_if_list_is_empty(app)
    if len(orm.get_groups_without_contacts()) == 0: #проверка: если пустых групп нет - создать
        app.group.create(Group(name="WOW_WOW"))

    contacts=orm.get_contacts_not_in_any_group() #берем контакт из списка без групп
    contact=random.choice(contacts)
    groups=orm.get_groups_without_contacts() #группа из пустых групп
    group=random.choice(groups)
    app.contact.add_contact_to_group_by_ids(contact, group)
    #validation
    contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
    if (contact not in contacts_in_group) or (group in list(orm.get_groups_without_contacts())):
        raise ValueError("ERROR: contact %s not found in group %s" % contact % group)



def create_if_list_is_empty(app):
    c=Contact(middlename="To_Group", lastname="To_Group", nickname="mln_mln", firstname="Jecka")
    app.open_page()
    app.contact.add_new()
    app.contact.fill_name(c)
    app.contact.submit()
    app.return_homepage()