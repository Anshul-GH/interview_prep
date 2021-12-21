from unittest import TestCase
from modules.square_preceding import square_preceding

class TestPower(TestCase):
    '''
    Test the function power_num from the module power.py
    '''
    def test_power_int_lst(self):
        self.assertEqual(square_preceding([1, 2, 3]), [0, 1, 4])
    
    def test_power_float_lst(self):
        self.assertEqual(square_preceding([1.1, 1.2, 1.3]), [0, 1.21, 1.44])

    def test_for_empty_list(self):
        self.assertEqual(square_preceding([]), [])
