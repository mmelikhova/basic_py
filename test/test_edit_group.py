from model.group import Group


def test_edit_first_group(app):
    app.session.login(login="admin", password="secret")
    app.group.edit_first_group(Group(groupname="edited_group", header_text="miu", footer_text="miu"))
    app.session.logout()

