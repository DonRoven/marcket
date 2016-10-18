import unittest
from datetime import date
from Cart import Cart
from User import User
from Item import Item

class DiscountsTestCase(unittest.TestCase):

    def setUp(self):
        self.user = User('username', 'askgha')
        self.cart = Cart(self.user)

    def tearDown(self):
        del self.cart
        del self.user

    def test_discount_gt_1000(self):
        self.cart.add(Item('item1', 100), 10)
        self.assertEqual(self.cart.discount(), 50)

    def test_discount_lt_1000(self):
        self.cart.add(Item('item1', 10), 10)
        self.assertEqual(self.cart.discount(), 3)

#    def test_discount_bday(self):
#        self.user = User('username', 'askgha', bday = date.today())
#        self.cart.add(Item('item1', 100))
#        self.assertEqual(self.cart.discount(), 10)
    def test_bday_discount(self):
        user = User('username', 'askgha', bday = date.today())
        cart = Cart(user)
        cart.add(Item('item1', 100))
        self.assertEqual(cart.discount(), 10)

if __name__ == '__main__':
    unittest.main()
