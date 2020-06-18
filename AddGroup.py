# -*- coding: utf-8 -*-
# author melikhova
from application import Application
import pytest
from group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(groupname="new_mln_group", header_text="hello", footer_text="hello"))
        app.logout()


def test_add_empty_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(groupname="", header_text="", footer_text=""))
        app.logout()
