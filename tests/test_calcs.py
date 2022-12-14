#Usage python -m unittest test_calcs.py

import unittest
import sys
sys.path.append('../unit_testing_with_python')
import functions.calcer as test_calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        print('Running addition test')
        self.assertEqual(test_calc.add(10,5), 15)
        self.assertEqual(test_calc.add(-1,1), 0)
        self.assertEqual(test_calc.add(-1,-1), -2)

    def test_subtract(self):
        print('Running subtract test')
        self.assertEqual(test_calc.subtract(10,5), 5)
        self.assertEqual(test_calc.subtract(-1,1), -2)
        self.assertEqual(test_calc.subtract(-1,-1), 0)

    def test_multiply(self):
        print('Running multiply test')
        self.assertEqual(test_calc.multiply(10,5), 50)
        self.assertEqual(test_calc.multiply(-1,1), -1)
        self.assertEqual(test_calc.multiply(-1,-1), 1)

    def test_divide(self):
        
        self.assertEqual(test_calc.divide(10,5), 2)
        self.assertEqual(test_calc.divide(-1,1), -1)
        self.assertEqual(test_calc.divide(-1,-1), 1)

        with self.assertRaises(ValueError):
            test_calc.divide(10,0)

# if __name__ == '__main__':
#    unittest.main()
