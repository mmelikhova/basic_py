from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(groupname="edited_group", header_text="miu", footer_text="miu"))


def test_edit_name_1group(app):
    app.group.modify_first_group(Group(groupname="edited_group_name"))


def test_edit_header_1group(app):
    app.group.modify_first_group(Group(header_text="edited_header_text"))

