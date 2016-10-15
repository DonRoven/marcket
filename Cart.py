from Item import Item
from collections import defaultdict
from datetime import date

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

    def discount(self):
        total = self.total()
        qt = self.total_qt()
        today = date.today()
        if hasattr(self.user, 'bday') and\
            today.month == self.user.bday.month and\
            today.day == self.user.bday.day:
            bday_discount = self. total() * 0.1
        else:
            bday_discount = 0
        qt_discount = total * .03 if qt >=10 else 0
        total_discount = total * .05 if total >= 1000 else 0
#        return max(qt_discount, total_discount, bday_discount)
        return max(total_discount, bday_discount)



#item1 = Item('item1', 10)
#item2 = Item('item2', 20)
#add(item1, 1)
#add(item2, 2)
#print(self._len)