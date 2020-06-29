from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(groupname="for_full_edition"))
    app.group.modify_first_group(Group(groupname="edited_group", header_text="miu", footer_text="miu"))


def test_edit_name_1group(app):
    if app.group.count() == 0:
        app.group.create(Group(groupname="for_name_edition"))
    app.group.modify_first_group(Group(groupname="edited_group_name"))


def test_edit_header_1group(app):
    if app.group.count() == 0:
        app.group.create(Group(groupname="for_header_edition", header_text="miu_for edition"))
    app.group.modify_first_group(Group(header_text="edited_header_text"))


def test_edit_footer_1group(app):
    if app.group.count() == 0:
        app.group.create(Group(groupname="for_header_edition", header_text="miu_for edition",
                               footer_text="miu_for edition"))
    app.group.modify_first_group(Group(footer_text="edited_footer_text"))

