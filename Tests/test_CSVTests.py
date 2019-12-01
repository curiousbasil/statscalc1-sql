import unittest
from CSVReader.CsvReader import CsvReader, classfactory


class MyTestCase(unittest.TestCase):
    pass

    def setUp(self) -> None:
        self.csv_reader = CsvReader(filepath='Tests/Data/Unit_Test_Statistics.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('Value 1')
        self.assertIsInstance(people, list)
        test_class = classfactory('Value 1', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__)


if __name__ == '__main__':
    unittest.main()
