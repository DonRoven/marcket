import unittest
from Item import Item


class ItemTestCase(unittest.TestCase):
    def test_basic(self):
        item = Item('product1', 100.5, type='red')
        self.assertEqual(item.name, 'product1')
        self.assertEqual(item.price, 100.5)
        self.assertEqual(item.type, 'red')

    def test_skip_optional(self):
        item = Item('product1', 100.5, size='M')
        self.assertFalse(hasattr(item, 'size'))


if __name__ == '__main__':
    unittest.main()
