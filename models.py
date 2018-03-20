import ast


class Apartment:
    def __init__(self, uid, bathrooms=None, bedrooms=None, building_id=None, created=None, description=None,
                 features=None, display_address=None, latitude=None, listing_id=None, longitude=None, manager_id=None,
                 photos=None, price=None, street_address=None, interest_level=None, ):
        self.id = uid
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.building_id = building_id
        self.created = created
        self.description = description
        self.features = features
        self.display_address = display_address
        self.latitude = latitude
        self.listing_id = listing_id
        self.longitude = longitude
        self.manager_id = manager_id
        self.photos = photos
        self.price = price
        self.street_address = street_address
        self.interest_level = interest_level

    def get_bathrooms(self):
        return self.bedrooms if self.bedrooms else 0

    def get_bedrooms(self):
        return self.bedrooms if self.bedrooms else 0

    def get_description(self):
        return self.description if self.description else ''

    def get_price(self):
        return self.price if self.price else 0

    def get_features(self):
        return ast.literal_eval(self.features)

    def get_photos(self):
        return ast.literal_eval(self.photos)

    def __str__(self):
        limited = {key: str(value)[:20] for key, value in self.__dict__.items()}
        return str(limited)
