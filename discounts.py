"""
Discount functions for shop models
All discounts take `Cart` instance as only argument
All discounts return flat discount value. More is better
`max_discount` should be used mainly from other modules
"""
from datetime import date


active_discounts = []


def active(func):
    """
    Decorator to mark up currently active discounts.
    Adds disocunt func to `active_discounts` list
    """
    active_discounts.append(func)
    return func


def max_discount(cart):
    """
    Returns best discount among all active discounts
    """
    return max(f(cart) for f in active_discounts)


@active
def qt_discount(cart):
    """
    3% discount for buying 10 or more items
    """
    return cart.total() * 0.03 if cart.total_qt() >= 10 else 0


@active
def total_discount(cart):
    """
    5% discount for orders with total value >= 1000
    """
    total = cart.total()
    return total * 0.05 if total >= 1000 else 0


@active
def bday_discount(cart):
    """
    10% discount for customers birthday
    """
    today = date.today()
    if hasattr(cart.user, 'bday') and \
        today.month == cart.user.bday.month and \
        today.day == cart.user.bday.day:
        return cart.total() * 0.1
    return 0
