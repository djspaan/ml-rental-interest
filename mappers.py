from models import Apartment


class ApartmentMapper:
    reader = None
    repository = None
    apartments = {}

    def __init__(self, reader, repository):
        self.reader = reader
        self.repository = repository

    def get_ids(self, items):
        ids = []
        for attr, values in items.items():
            for key, value in values.items():
                ids.append(key)
        return sorted(set(ids))

    def init_items(self, ids):
        for uid in ids:
            self.apartments[int(uid)] = Apartment(uid)

    def read(self):
        items = self.reader.get_items()
        self.init_items(self.get_ids(items))
        for attr, values in items.items():
            for uid, value in values.items():
                setattr(self.apartments[int(uid)], attr, value)

    def insert(self):
        i = 1
        for key, apartment in self.apartments.items():
            print('inserting apartments: %d %%' % (i / len(self.apartments) * 100))
            self.repository.create(apartment)
            i = i + 1

    def map_to_db(self):
        # TODO: Validate if user wants to drop db
        self.repository.refresh()
        self.read()
        self.insert()

        #
        # app = Apartment(1)
        # app.manager_id = 'sdsdfsfd213'
        # app.price = '2400'
        # app.photos = 'sdfsdffsdf[dfdsfssdf]sdfsdfsdf""sdfsdfsdf'
        # app.description = self.apartments[4].description
        # app.features = self.apartments[4].features
        # print()
        # self.repository.create(app)

        # print(self.apartments)
        # self.insert()
        #
        # for key, value in items[].items():
        #     print(items[key])