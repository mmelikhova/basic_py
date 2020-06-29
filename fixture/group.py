class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_gr_page(self):
        wd=self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
            wd = self.app.wd
            wd.find_element_by_link_text("group page").click()

    def group_form(self, group):
        wd = self.app.wd
        # fill group form
        self.change_field_value("group_name", group.groupname)
        self.change_field_value("group_header", group.header_text)
        self.change_field_value("group_footer", group.footer_text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, group):
            # create new group
            wd = self.app.wd
            self.open_gr_page()
            wd.find_element_by_name("new").click()
            self.group_form(group)
            wd.find_element_by_name("submit").click()
            self.return_to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_gr_page()
        #select 1st group
        wd.find_element_by_name("selected[]").click()
        #submit delete
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_gr_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def count(self):
        wd = self.app.wd
        self.open_gr_page()
        return len(wd.find_elements_by_name("selected[]"))




