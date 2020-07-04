
class Group:

    def __init__(self, groupname=None, header_text=None, footer_text=None, id = None):
        self.groupname = groupname
        self.header_text = header_text
        self.footer_text = footer_text
        self.id = id

    def __repr__(self):
        return "%s: %s" % (self.id, self.groupname)

    def __eq__(self, other):
        return self.id == other.id and self.groupname == other.groupname
