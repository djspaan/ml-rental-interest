class Collection:
    items = []

    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items

    def all(self):
        return self.items

    def count(self):
        return len(self.items)

    def add(self, item):
        self.items.append(item)

    def pluck(self, attribute):
        return [getattr(item, attribute) for item in self.items]

    def first(self):
        return self.items[0]

    def take(self, amount):
        return Collection(self.items[0:amount])

    def map(self, callback):
        return {str(item): callback(item) for item in self.items}

    def __getitem__(self, key):
        return self.items[key]

    def __str__(self):
        return '\n'.join(map(str, self.items))


class ApartmentCollection(Collection):
    def __init__(self, items=None):
        Collection.__init__(self, items)

    def where(self, key, value):
        items = [item for item in self.items if getattr(item, key) == value]
        return ApartmentCollection(items)
