import unittest
from utilities.basic_math import check_even, add_numbers


class MyTest(unittest.TestCase):   

    def test_check_even(self):
        test_data = 8
        self.assertTrue(check_even(test_data))


    def test_add_numbers(self):
       test_num_1 = 6
       test_num_2 = 7
       expected = 13
       self.assertEqual(expected, add_numbers(test_num_1, test_num_2))
       

if __name__ == '__main__':
    unittest.main()