
class Contact:

    def __init__(self, note, phone2, home_address, homepage,
                 mail1, mail2, mail3, title_text,
                 firstname, middlename, lastname, nickname,
                 company_address, company,
                 ayear, amonth, aday, byear, bmonth, bday,
                 home_num, mob_num, work_num, fax_num):
        self.title_text = title_text
        self.fax_num = fax_num
        self.work_num = work_num
        self.mob_num = mob_num
        self.home_num = home_num
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
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