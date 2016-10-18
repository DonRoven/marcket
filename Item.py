class Item(object):
    optional_fields = {'img', 'description', 'type'}

    def __init__(self, name, price, **kwargs):
        self.name = name
        self.price = price
        for field in kwargs:
            if field in Item.optional_fields:
                setattr(self, field, kwargs[field])

    def __hash__(self):
        """
        Gives ability to use `Item` instance in `dict` as key.
        `__eq__` should be defined to resolve possible collisions
        """
        return hash((self.name, self.price))

    def __eq__(self, other):
        """
        If used as `dict` key, `__eq__` should be provided to
            catch possible hashing collisions.
        Goes together with `__hash__`
        """
        return self.name == other.name and self.price == other.price
