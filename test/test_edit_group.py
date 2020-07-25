from model.group import Group
import random


def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="for_edit"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    g = Group(name="edited", header="edited", footer='edited_too')
    app.group.modify_group_by_id(g, group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(g)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)