# -*- coding: utf-8 -*-
# author melikhova

import pytest
from model.group import Group


def test_add_group(app):
        app.group.create(Group(groupname="hh", header_text="hello", footer_text="hello"))


def test_add_empty_group(app):
        app.group.create(Group(groupname="", header_text="", footer_text=""))

