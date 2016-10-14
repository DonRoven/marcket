from Item import Item
from collections import defaultdict


class Cart:
    def __init__(self, user):
        self.user = user
        self._items = defaultdict(int)

    def total(self):
        return sum(item.price * qt for item, qt in self._items.items())

    def add(self, item, quantity = 1):
        self._items[item] += quantity

    def __len__(self):
        return len(self._items)

    def total_qt(self):
        return sum(self._items.values())

    def __iter__(self):
        return iter(self._items)

#item1 = Item('item1', 10)
#item2 = Item('item2', 20)
#add(item1, 1)
#add(item2, 2)
#print(self._len)