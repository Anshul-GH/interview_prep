from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        valid_triplets = set()

        # iterate over all possible triplets
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i+1, len_nums):
                for k in range(j+1, len_nums):
                    valid_triplets.add([nums[i], nums[j], nums[k]])

        return list(valid_triplets)


# if __name__ == "__main__":
#     print("Add body to main")
