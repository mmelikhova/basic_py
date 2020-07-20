# -*- coding: utf-8 -*-
# mmelikhova

import pytest
from model.contact import Contact
import random
import string



def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
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
    app.homepage()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts=app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

