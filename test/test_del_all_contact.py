
def test_delete_all_contact(app):
    app.open_page()
    app.session.login(login="admin", password="secret")
    app.contact.delete_all_contact()
    app.session.logout()