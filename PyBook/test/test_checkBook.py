from unittest import TestCase

from .. import Containers
from .. import checkbook


class TestCheckBook(TestCase):
    def setUp(self):
        self.t = Containers.Transaction(1, "first", "category", "today", 5)

    def test_main(self):
        one = self.t.name == "first"
        two = self.t.number == 1
        thr = self.t.category == "category"
        fou = self.t.date == "today"
        fiv = self.t.value == 5
        six = one and two and thr and fou and fiv
        self.failUnless(six)

    def test_add(self):
        cb = checkbook.CheckBook()
        cmd = ['', 'First', 'Category', 5]
        cb.add(cmd)
        print(cb.categories)
        print(cb.amounts)
        self.failUnless(cb.categories[0] == 'Category' and cb.amounts[0] == 5)
