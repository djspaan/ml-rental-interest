from readers import JSONReader
from mappers import ApartmentMapper
from repositories import ApartmentRepository
from connectors import SQLite
from algorithms import *


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
        Main.tree(apartments)

    @staticmethod
    def tree(apartments):
        """
        Use a CART decision tree to evaluate the given apartments.
        :param apartments:
        """
        dataset = apartments.map(
            lambda a: [float(a.get_bathrooms()), float(a.get_bedrooms()), float(len(a.get_description())),
                       float(a.get_price()), float(len(a.get_features())), a.interest_level])[:1000]

        n_folds = 5
        max_depth = 5
        min_size = 10
        scores = evaluate_algorithm(dataset, decision_tree, n_folds, max_depth, min_size)
        print('Scores: %s' % scores)
        print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

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
