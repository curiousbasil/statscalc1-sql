import unittest
from Statistics.Statistics import Statistics
from CSVReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        test_data = CsvReader('Tests/Data/Unit_Test_Statistics.csv').data
        for row in test_data:
            result = float(row['mean1'])
            self.assertEqual(self.statistics.mean(row['ds1_value1'], row['ds1_value2'], row['ds1_value3'],
                                                  row['ds1_value4'], row['ds1_value5'], row['ds1_value6'],
                                                  row['ds1_value7'], row['ds1_value8'], row['ds1_value9'],
                                                  row['ds1_value10']), result)
            self.assertEqual(self.statistics.result, result)
            pprint(test_data)

    def test_sample_mean(self):
        test_data = CsvReader('Tests/Data/Unit_Test_Statistics.csv').data
        for row in test_data:
            result = float(row['smean1'])
            self.assertEqual(self.statistics.sample_mean(row['ds1_value1'], row['ds1_value2'], row['ds1_value3'],
                                                  row['ds1_value4'], row['ds1_value5']), result)
            self.assertEqual(self.statistics.result, result)
            pprint(test_data)

    def test_median(self):
        test_data = CsvReader('Tests/Data/Unit_Test_Statistics.csv').data
        for row in test_data:
            result = float(row['median1'])
            self.assertEqual(self.statistics.median(row['ds1_value1'], row['ds1_value2'], row['ds1_value3'],
                                                    row['ds1_value4'], row['ds1_value5'], row['ds1_value6'],
                                                    row['ds1_value7'], row['ds1_value8'], row['ds1_value9']), result)
            self.assertEqual(self.statistics.result, result)

    def test_mode(self):
        test_data = CsvReader('Tests/Data/Unit_Test_Statistics.csv').data
        for row in test_data:
            result = float(row['mode1'])
            self.assertEqual(self.statistics.mode(row['ds1_value1'], row['ds1_value2'], row['ds1_value3'],
                                                  row['ds1_value4'], row['ds1_value5'], row['ds1_value6'],
                                                  row['ds1_value7'], row['ds1_value8'], row['ds1_value9'],
                                                  row['ds1_value10']), result)
            self.assertEqual(self.statistics.result, result)

    def test_variance(self):
        test_data = CsvReader('Tests/Data/Unit_Test_Statistics.csv').data
        for row in test_data:
            result = float(row['var1'])
            self.assertEqual(self.statistics.variance(row['ds1_value1'], row['ds1_value2'], row['ds1_value3'],
                                                      row['ds1_value4'], row['ds1_value5'], row['ds1_value6'],
                                                      row['ds1_value7'], row['ds1_value8'], row['ds1_value9'],
                                                      row['ds1_value10']), result)
            self.assertEqual(self.statistics.result, result)

    def test_pvariance(self):
        test_data = CsvReader('Tests/Data/Unit_Test_Statistics.csv').data
        for row in test_data:
            result = float(row['popvar1'])
            self.assertEqual(self.statistics.pvariance(row['ds1_value1'], row['ds1_value2'], row['ds1_value3'],
                                                      row['ds1_value4'], row['ds1_value5'], row['ds1_value6'],
                                                      row['ds1_value7'], row['ds1_value8'], row['ds1_value9'],
                                                      row['ds1_value10']), result)
            self.assertEqual(self.statistics.result, result)

    def test_standarddeviation(self):
        test_data = CsvReader('Tests/Data/Unit_Test_Statistics.csv').data
        for row in test_data:
            result = float(row['pop_std_dev1'])
            self.assertEqual(self.statistics.standarddeviation(row['ds1_value1'], row['ds1_value2'], row['ds1_value3'],
                                                      row['ds1_value4'], row['ds1_value5'], row['ds1_value6'],
                                                      row['ds1_value7'], row['ds1_value8'], row['ds1_value9'],
                                                      row['ds1_value10']), result)
            self.assertEqual(self.statistics.result, result)


    def test_zscore(self):
        test_data = CsvReader('Tests/Data/Unit_Test_Statistics.csv').data
        for row in test_data:
            result = float(row['zscoreresult'])
            self.assertEqual(self.statistics.zscore(row['ds1_value1'], row['zmean'], row['zstdev']), result)
            self.assertEqual(self.statistics.result, result)

    def test_results_property(self):
        self.assertEqual(self.statistics.result, 0)


if __name__ == '__main__':
    unittest.main()
