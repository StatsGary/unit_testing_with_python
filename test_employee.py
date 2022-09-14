#Usage python -m unittest test_employee.py

import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setup Class')

    @classmethod
    def tearDownClass(cls):
        print('Tear down class')


    def setUp(self):
        # Instance attributes
        self.emp1 = Employee('Gary', 'Hutson', 50000)
        self.emp2 = Employee('Jamie', 'Pipersand', 45000)

    def tearDown(self):
        # Files to a directory and database to delete the files
        pass

    def test_email(self):
        self.assertEqual(self.emp1.email, 'Gary.Hutson@email.com')
        self.assertEqual(self.emp2.email,'Jamie.Pipersand@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, 'Gary Hutson')
        self.assertEqual(self.emp2.fullname, 'Jamie Pipersand')

    def test_apply_raise(self):
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.salary, 52500)
        self.assertEqual(self.emp2.salary, 47250)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Hutson/May')
            self.assertEqual(schedule, 'Success')

            # Check for bad response
            mocked_get.return_value.ok = False
            schedule = self.emp2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Pipersand/June')
            self.assertEqual(schedule, 'Bad response!')

# if __name__ == '__main__':
#     unittest.main()