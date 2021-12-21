from modules.my_functions import multiply_two_numbers_better, multiply_two_numbers
import unittest

# class TestMultiply(unittest.TestCase):
#     def test_with_two_positives(self):
#         self.assertEqual(multiply_two_numbers(17, 19), 17 * 19)
#         self.assertEqual(multiply_two_numbers(12627327, 9883762), 12627327 * 9883762)
#         self.assertEqual(multiply_two_numbers(1, 2), 2)

#     def test_with_one_zero(self):
#         self.assertEqual(multiply_two_numbers(17, 0), 0)
#         self.assertEqual(multiply_two_numbers(0, 9883762), 0)

#     def test_with_two_zeros(self):
#         self.assertEqual(multiply_two_numbers(0, 0), 0)

#     def test_with_one_negative(self):
#         self.assertEqual(multiply_two_numbers(-17, 19), (-17) * 19)
#         self.assertEqual(multiply_two_numbers(12627327, -9883762), 12627327 * (-9883762))

#     def test_with_two_negatives(self):
#         self.assertEqual(multiply_two_numbers(-17, -19), 17 * 19)
#         self.assertEqual(multiply_two_numbers(-12627327, -9883762), 12627327 * 9883762)

class TestMultiplyBetter(unittest.TestCase):
    def test_with_two_positives(self):
        self.assertEqual(multiply_two_numbers_better(17, 19), 17 * 19)
        self.assertEqual(multiply_two_numbers_better(12627327, 9883762), 12627327 * 9883762)
        self.assertEqual(multiply_two_numbers_better(1, 2), 2)

    def test_with_one_zero(self):
        self.assertEqual(multiply_two_numbers_better(17, 0), 0)
        self.assertEqual(multiply_two_numbers_better(0, 9883762), 0)

    def test_with_two_zeros(self):
        self.assertEqual(multiply_two_numbers_better(0, 0), 0)

    def test_with_one_negative(self):
        self.assertEqual(multiply_two_numbers_better(-17, 19), (-17) * 19)
        self.assertEqual(multiply_two_numbers_better(12627327, -9883762), 12627327 * (-9883762))

    def test_with_two_negatives(self):
        self.assertEqual(multiply_two_numbers_better(-17, -19), 17 * 19)
        self.assertEqual(multiply_two_numbers_better(-12627327, -9883762), 12627327 * 9883762)
