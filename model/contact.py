from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, note=None, phone2=None,
                 home_address=None, homepage=None,
                 mail1=None, mail2=None, mail3=None, title_text=None,
                 nickname=None,
                 company_address=None, company=None,
                 ayear=None, amonth=None, aday=None, byear=None, bmonth=None, bday=None,
                 home_num=None, mob_num=None, work_num=None, fax_num=None, cid=None):
        self.cid=cid
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.title_text = title_text
        self.fax_num = fax_num
        self.work_num = work_num
        self.mob_num = mob_num
        self.home_num = home_num
        self.nickname = nickname
        self.company = company
        self.company_address = company_address
        self.mail1 = mail1
        self.mail2 = mail2
        self.mail3 = mail3
        self.homepage = homepage
        self.home_address = home_address
        self.phone2 = phone2
        self.note = note
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear

    def __repr__(self):
        return "%s: %s: %s" % (self.cid, self.lastname, self.firstname)

    def __eq__(self, other):
        return ((self.cid is None
                or other.cid is None
                or self.cid == other.сid)
                and self.lastname == other.lastname
                and self.firstname == other.firstname)

    def id_or_max(self):
        if self.cid:
            return int(self.cid)
        else:
            return maxsize
