from containers import ApartmentCollection
from models import Apartment


class ApartmentRepository:
    db = None

    def __init__(self, db):
        self.db = db

    def all(self):
        apartments = ApartmentCollection()
        ap_rows = self.db.fetch('SELECT * FROM APARTMENT').fetchall()
        for ap_row in ap_rows:
            apartments.add(Apartment(*ap_row))
        return apartments

    def first(self):
        ap_row = self.db.fetch('SELECT * FROM APARTMENT').fetchone()
        return Apartment(*ap_row)

    def refresh(self):
        self.db.execute('DROP TABLE APARTMENT')
        self.db.execute('CREATE TABLE APARTMENT (ID INT PRIMARY KEY NOT NULL, BATHROOMS INT, BEDROOMS INT, BUILDING_ID TEXT, CREATED TEXT, DESCRIPTION TEXT, FEATURES TEXT, DISPLAY_ADDRESS TEXT, LATITUDE REAL, LISTING_ID INT, LONGITUDE REAL, MANAGER_ID TEXT, PHOTOS TEXT, PRICE REAL, STREET_ADDRESS TEXT, INTEREST_LEVEL TEXT);')

    def create(self, apartment):
        self.db.execute('''INSERT INTO APARTMENT (ID, BATHROOMS, BEDROOMS, BUILDING_ID, CREATED, DESCRIPTION, FEATURES, DISPLAY_ADDRESS, LATITUDE, LISTING_ID, LONGITUDE, MANAGER_ID, PHOTOS, PRICE, STREET_ADDRESS, INTEREST_LEVEL)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                        (
                            int(apartment.id) if apartment.id else None,
                            int(apartment.bathrooms) if apartment.bathrooms else None,
                            int(apartment.bedrooms) if apartment.bedrooms else None,
                            str(apartment.building_id),
                            str(apartment.created),
                            str(apartment.description),
                            str(apartment.features),
                            str(apartment.display_address),
                            float(apartment.latitude) if apartment.latitude else None,
                            str(apartment.listing_id),
                            float(apartment.longitude) if apartment.longitude else None,
                            str(apartment.manager_id),
                            str(apartment.photos),
                            float(apartment.price) if apartment.price else None,
                            str(apartment.street_address),
                            str(apartment.interest_level)
                        )
                        )

    def update(self, uid, key, value):
        self.db.execute('UPDATE APARTMENT SET %s = ? WHERE id = ?' % key, (value, uid))
