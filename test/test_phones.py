import re


def test_phones_on_home_page(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_editpage = app.contact.get_contact_info_from_editpage(0)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_homepage(contact_from_editpage)


def test_phones_on_contact_view_page(app):
    contact_from_viewpage=app.contact.get_contact_info_from_viewpage()[0]
    contact_from_editpage=app.contact.get_contact_info_from_editpage(0)
    assert contact_from_viewpage.home_num == contact_from_editpage.home_num
    assert contact_from_viewpage.work_num == contact_from_editpage.work_num
    assert contact_from_viewpage.mob_num == contact_from_editpage.mob_num
    assert contact_from_viewpage.phone2 == contact_from_editpage.phone2


def clear(s):
    return re.sub("[() -+]", "", s)


def merge_phones_like_homepage(contact):
    "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x), filter(lambda x: x is not None, [contact.home_num, contact.mob_num,
                                              contact.work_num, contact.phone2]))))
