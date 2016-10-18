import unittest
from datetime import date
from Cart import Cart
from User import User
from Item import Item
from unittest.mock import Mock
from discounts import bday_discount

class DiscountsTestCase(unittest.TestCase):

    def setUp(self):
        self.user = User('username', 'askgha')
        self.cart = Cart(self.user)

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
        cart = Mock()
        cart.user.bday = date.today()
        cart.total.return_value = 100
        self.assertEqual(bday_discount(cart), 10)

if __name__ == '__main__':
    unittest.main()
