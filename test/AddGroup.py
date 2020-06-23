# -*- coding: utf-8 -*-
# author melikhova

import pytest
from model.group import Group


def test_add_group(app):
        app.session.login(login="admin", password="secret")
        app.group.create(Group(groupname="hh", header_text="hello", footer_text="hello"))
        app.session.logout()


def test_add_empty_group(app):
        app.session.login(login="admin", password="secret")
        app.group.create(Group(groupname="", header_text="", footer_text=""))
        app.session.logout()
