class Contact:

    def __init__(self, firstname, middlename, lastname, nickname):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname


class Title:
    def __init__(self, title):
        self.title = title


class Company:
    def __init__(self, company_address, company):
        self.company = company
        self.company_address = company_address


class Mail:
    def __init__(self, mail1, mail2, mail3):
        self.mail1 = mail1
        self.mail2 = mail2
        self.mail3 = mail3


class Homepage:
    def __init__(self, homepage):
        self.homepage = homepage


class Homeaddress:
    def __init__(self, home_address):
        self.home_address = home_address


class Homephone:
    def __init__(self, phone2):
        self.phone2 = phone2


class Note:
    def __init__(self, note):
        self.note = note
