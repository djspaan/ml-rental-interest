from readers import JSONReader
from mappers import ApartmentMapper
from repositories import ApartmentRepository
from connectors import SQLite

# from analyzers import ApartmentAnalyzer

APARTMENT_FILE = './data/train.json'


class Main:
    def __init__(self):
        pass

    @staticmethod
    def run():
        """
        Main function of the system.
        """
        connection = SQLite('data/train.db')
        repository = ApartmentRepository(connection)
        apartments = repository.all()
        print(apartments)

    @staticmethod
    def map():
        """
        Use this function to map the json data to a sqlite database.
        """
        connection = SQLite('data/train.db')
        reader = JSONReader(APARTMENT_FILE)
        repository = ApartmentRepository(connection)
        mapper = ApartmentMapper(reader, repository)
        mapper.map_to_db()


if __name__ == '__main__':
    Main.run()
