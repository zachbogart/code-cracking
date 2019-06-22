from unittest import TestCase


class TestIs_unique(TestCase):
    def test_hello(self):
        from is_unique import is_unique
        self.assertFalse(is_unique("hello"))

    def test_helo(self):
        from is_unique import is_unique
        self.assertTrue(is_unique("helo"))


class TestIs_unique_improved(TestCase):
    def test_hello(self):
        from is_unique import is_unique
        self.assertFalse(is_unique("hello"))

    def test_helo(self):
        from is_unique import is_unique
        self.assertTrue(is_unique("helo"))
