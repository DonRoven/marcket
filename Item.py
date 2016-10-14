class Item:
    optional_fields = {'img', 'description', 'type'}

    def __init__(self, name, price, **kwargs):
        self.name = name
        self.price = price
        for field in kwargs:
            if field in Item.optional_fields:
                setattr(self, field, kwargs[field])

    def __hash__(self):
        return hash((self.name, self.price))
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price
