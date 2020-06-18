# -*- coding: utf-8 -*-
# author melikhova

import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(groupname="2_mln_group", header_text="hello", footer_text="hello"))
        app.session.logout()


def test_add_empty_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(groupname="", header_text="", footer_text=""))
        app.session.logout()
