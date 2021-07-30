import unittest
from src.Calculator.Calculator import Calculator
from src.CsvReader.csvReader import CsvReader


class MyTestCase(unittest.TestCase):    # unit tests are tests we write to test code. (TDD) test driven development
    def setUp(self) -> None:
        self.calculator = Calculator()  # instantiates calculator in each test.

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)    # tests if there is a calculator (instance, isItAClass?)
        print("Completed Calc Instantiate Test ")

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)
        print("Completed Calc Property Test")

    def test_add_method_calculator(self):
        print("Beginning Addition Test")
        test_data_add = CsvReader('src/Tests/Data/Unit Test Addition.csv').data
        for row in test_data_add:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
        print("Completed Addition Test")

    def test_subtract_method_calculator(self):
        print("Beginning Subtraction Test")
        test_data_subtract = CsvReader('src/Tests/Data/Unit Test Subtraction.csv').data
        for row in test_data_subtract:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
        print("Completed Subtraction Test")

    def test_multiplication_method_calculator(self):
        print("Beginning Multiplication Test")
        test_data_multiply = CsvReader('src/Tests/Data/Unit Test Multiplication.csv').data
        for row in test_data_multiply:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
        print("Completed Multiplication Test")

    def test_division_method_calculator(self):
        print("Beginning Division Test")
        test_data_divide = CsvReader('src/Tests/Data/Unit Test Division.csv').data
        for row in test_data_divide:
            self.assertAlmostEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
        print("Completed Division Test")

    def test_division_method_calculator_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(0, 1)

    def test_square_method_calculator(self):
        print("Beginning Square Test")
        test_data_square = CsvReader('src/Tests/Data/Unit Test Square.csv').data
        for row in test_data_square:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
        print("Completed Square Test")

    def test_sqrt_method_calculator(self):
        print("Beginning Square Root Test")
        test_data_sqrt = CsvReader('src/Tests/Data/Unit Test Square Root.csv').data
        for row in test_data_sqrt:
            self.assertAlmostEqual(self.calculator.sqrt(row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))
        print("Completed Square Root Test")

    def test_sqrt_negatives_method_calculator(self):
        with self.assertRaises(ValueError):
            self.calculator.sqrt(-25)


if __name__ == '__main__':
    unittest.main()
