from collections import defaultdict
from discounts import max_discount


class Cart(object):
    """
    Basic model for customers order
    """

    def __init__(self, user):
        self.user = user
        self._items = defaultdict(int)

    def total(self):
        """
        Returns cumulative value of all items in order
        """
        return sum(item.price * qt for item, qt in self._items.items())

    def add(self, item, quantity = 1):
        self._items[item] += quantity

    def __len__(self):
        """
        Returns number of distinct items in order
        """
        return len(self._items)

    def total_qt(self):
        """
        Returns physical number of ordered items
        """
        return sum(self._items.values())

    def __iter__(self):
        return iter(self._items)

    def discount(self):
        """
        Returns best available discount for current order
        """
        return max_discount(self)
