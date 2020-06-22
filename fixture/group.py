class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
            wd = self.app.wd
            wd.find_element_by_link_text("group page").click()

    def create(self, group):
            # create new group
            wd = self.app.wd
            self.app.open_gr_page()
            wd.find_element_by_name("new").click()
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.groupname)
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header_text)
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer_text)
            wd.find_element_by_name("submit").click()
            self.return_to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.app.open_gr_page()
        #select 1st group
        wd.find_element_by_name("selected[]").click()
        #submit delete
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.app.open_gr_page()
        # select 1st group
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.groupname)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header_text)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer_text)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

