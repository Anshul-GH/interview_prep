from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        underscores = 0
        while counter < len(nums):
            if nums[counter] == val:
                nums.remove(val)
                counter -= 1
                nums.append("_")
                underscores += 1
            counter += 1

        return (len(nums) - underscores)
