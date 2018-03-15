from readers import JSONReader
from mappers import ApartmentMapper
from repositories import ApartmentRepository
from connectors import SQLite


class Main:
    def __init__(self):
        pass

    @staticmethod
    def run():
        """
        Main routine of the system.
        """
        connection = SQLite('data/train.db')
        repository = ApartmentRepository(connection)
        apartments = repository.all()
        print(apartments)

    @staticmethod
    def map():
        """
        Use this function to map the json data to a sqlite database.
        Make sure the json data file and the database are available.
        """
        connection = SQLite('data/test.db')
        reader = JSONReader('data/test.json')
        repository = ApartmentRepository(connection)
        mapper = ApartmentMapper(reader, repository)
        mapper.map_to_db()


if __name__ == '__main__':
    # Main.map()
    Main.run()
