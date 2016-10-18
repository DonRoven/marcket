import unittest
from Cart import Cart
from User import User
from Item import Item


class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.user = User('username', 'askgha')
        self.cart = Cart(self.user)

    def tearDown(self):
        del self.cart
        del self.user

    def test_init(self):
        self.assertIs(self.cart.user, self.user)

    def test_total_empty_cart(self):
        self.assertEqual(self.cart.total(), 0)

    def test_total_non_empty(self):
        item = Item('item1', 10)
        self.cart.add(item)
        self.assertNotEqual(self.cart.total(), 0)
        self.assertEqual(self.cart.total(), 10)

    def test_total_two_different_items(self):
        item1 = Item('item1', 10)
        item2 = Item('item2', 20)
        self.cart.add(item1, 1)
        self.cart.add(item2, 2)
        self.assertEqual(self.cart.total(), 50)

    def test_total_multiple_items(self):
        item = Item('item1', 10)
        self.cart.add(item, 2)
        self.assertEqual(self.cart.total(), 20)

    def test_multiadd(self):
        item = Item('item1', 10)
        self.cart.add(item, 1)
        self.cart.add(item, 2)
        self.assertEqual(self.cart.total(), 30)

    def test_add(self):
        item = Item('item100500', 42)
        self.assertIs(self.cart.add(item, 1), None)

    def test_add_same(self):
        item1 = Item('item1', 10)
        item2 = Item('item1', 10)
        self.cart.add(item1)
        self.cart.add(item2)
        self.assertEqual(len(self.cart._items), 1)

    def test_cart_len(self):
        self.assertEqual(len(self.cart), 0)
        self.cart.add(Item('item1', 10))
        self.assertEqual(len(self.cart), 1)

    def test_cart_qt(self):
        self.assertEqual(self.cart.total_qt(), 0)
        self.cart.add(Item('item1', 10), 2)
        self.assertEqual(self.cart.total_qt(), 2)
        self.cart.add(Item('item2', 20), 5)
        self.assertEqual(self.cart.total_qt(), 7)

    def test_iteration(self):
        self.cart.add(Item('item1', 10), 1)
        self.cart.add(Item('item2', 20), 2)
        self.assertEqual(sum(i.price for i in self.cart), 30)

if __name__ == '__main__':
    unittest.main()
