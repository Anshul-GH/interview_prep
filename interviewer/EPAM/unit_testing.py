import unittest

class TestingSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([2,3,5]), 10, "Sum should be 10.")
    
    def test_sum_tuple(self):
        self.assertEqual(sum([2,3,5]), 10, "Sum should be 10.")

if __name__ == "__main__":
    unittest.main()


# abc.py
def myadd(a, b):
    return a+b

# Write the unit test code for the above