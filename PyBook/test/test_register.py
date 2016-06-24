from unittest import TestCase

from .. import Containers
from .. import Finance


class TestRegister(TestCase):
    def setUp(self):
        self.t = []
        x = Containers.Transaction(0, "stuff", "none", "today", 5)
        self.t.append(x)

    def test_get_total(self):
        r = Finance.Register()
        s = r.get_total(self.t)
        self.failUnless(s == 5)
