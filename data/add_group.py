import pytest
from model.group import Group
import random
import string


constant = [
    Group(groupname= 'name1', header_text='header1', footer_text='footer1'),
    Group(groupname= 'name2', header_text='header2', footer_text='footer2')
]


def random_string(prefix, maxlen):
    symbols=string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata=[Group(groupname="", header_text="", footer_text="")] + [
    Group(groupname=random_string("name", 10), header_text=random_string("head", 20),
          footer_text=random_string("foot", 20))
    for i in range(3)
]

