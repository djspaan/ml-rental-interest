from readers import JSONReader
from mappers import ApartmentMapper
from repositories import ApartmentRepository
from connectors import SQLite
from algorithms import *
from random import shuffle
from containers import ApartmentCollection


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
        low = apartments.where('interest_level', 'low').take(3839)

        medium = apartments.where('interest_level', 'medium').take(3839)

        high = apartments.where('interest_level', 'high').take(3839)

        apartments = ApartmentCollection(low.items + medium.items + high.items)

        dataset = apartments.map(
            lambda a: [float(a.get_bathrooms()),
                       float(a.get_bedrooms()),
                       float(a.get_created()),
                       float(len(a.get_description())),
                       float(a.get_price()),
                       float(len(a.get_features())),
                       float(a.get_latitude()),
                       float(a.get_longitude()),
                       a.interest_level])

        shuffle(dataset)

        print(len(dataset))

        n_folds = 5
        max_depth = 8
        min_size = 10

        print('Max depth ' + str(max_depth))
        scores = evaluate_algorithm(dataset, decision_tree, n_folds, max_depth, min_size)
        print('Scores: %s' % scores)
        print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))

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
