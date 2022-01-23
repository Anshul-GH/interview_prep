from sqlalchemy import func
from solutions.arr_contains_duplicate import Solution
import unittest

class TestArrContDuplicates(unittest.TestCase):
    def test_array_with_duplicates(self):
        funct = Solution()
        arr = [1,2,3,4,5,6,7,0,9,8,7,6,5,4,2]
        assert(funct.containsDuplicate(arr), True)

    def test_array_without_duplicates(self):
        funct = Solution()
        arr = [1,2,3,4,5,6,7,0,9,8]
        assert(funct.containsDuplicate(arr), False)
