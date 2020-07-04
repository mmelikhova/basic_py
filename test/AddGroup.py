# -*- coding: utf-8 -*-
# author melikhova

import pytest
from model.group import Group


def test_add_group(app):
        old_groups = app.group.get_group_list()
        app.group.create(Group(groupname="hh", header_text="hello", footer_text="hello"))
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
        old_groups=app.group.get_group_list()
        app.group.create(Group(groupname="", header_text="", footer_text=""))
        new_groups=app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)

