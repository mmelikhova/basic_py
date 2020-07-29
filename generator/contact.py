import pytest
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as error:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o == "-f":
        f=a


def random_string(prefix, maxlen):
    symbols=string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


month_list=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
            'November', 'December']



testdata= [Contact(note=random_string("note", 20),
                                             phone2=random_string("ph2", 10),
                                             home_address=random_string("homeadd", 20),
                                             homepage=random_string("homepage", 20),
                                             middlename=random_string("midn", 25), lastname=random_string("lastn", 25),
                                             nickname=random_string("nick", 25), firstname=random_string("firstn", 25),
                                             company_address=random_string("compadd", 35),
                                             company=random_string("compname", 20),
                                             home_num=random_string("homeph", 10), mob_num=random_string("mobph", 10),
                                             work_num=random_string("workph", 10), fax_num=random_string("fax", 10),
                                             mail1=random_string("1mail", 20), mail2=random_string("2mail", 20),
                                             mail3=random_string("3mail", 20),
                                             bday=str(random.randrange(0, 31, 1)), bmonth=random.choice(month_list),
                                             byear=str(random.randrange(1900, 2020, 1)),
                                             aday=str(random.randrange(0, 31, 1)), amonth=random.choice(month_list),
                                             ayear=str(random.randrange(1900, 2020, 1)),
                                             title_text=random_string("title", 10))
                                     for i in range(n)
                                     ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))