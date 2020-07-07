from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(groupname="for_full_edition"))
    old_groups=app.group.get_group_list()
    app.group.modify_first_group(Group(groupname="edited_group", header_text="miu", footer_text="miu"))
    new_groups=app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)


def test_edit_name_1group(app):
    if app.group.count() == 0:
        app.group.create(Group(groupname="for_name_edition"))
    old_groups = app.group.get_group_list()
    group = Group(groupname="edited_group_name")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_header_1group(app):
    if app.group.count() == 0:
        app.group.create(Group(groupname="for_header_edition", header_text="miu_for edition"))
    old_groups=app.group.get_group_list()
    app.group.modify_first_group(Group(header_text="edited_header_text"))
    new_groups=app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_footer_1group(app):
    if app.group.count() == 0:
        app.group.create(Group(groupname="for_header_edition", header_text="miu_for edition",
                               footer_text="miu_for edition"))
    old_groups=app.group.get_group_list()
    app.group.modify_first_group(Group(footer_text="edited_footer_text"))
    new_groups=app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

