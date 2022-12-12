# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index_next_larger = -1

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                index_next_larger = i

        # if arr is already reversed sorted
        if index_next_larger == -1:
            nums.sort()
            return nums

        index_second_larger = -1
        for i in range(len(nums)):
            if nums[index_next_larger] < nums[i]:
                index_second_larger = i

        # swap values
        nums[index_next_larger], nums[index_second_larger] = nums[index_second_larger], nums[index_next_larger]

        # reverse the sub-array nums[index_next_larger+1:]
        nums[index_next_larger+1:] = reversed(nums[index_next_larger+1:])

        return nums


# class Solution:
#     def permutations(self, lst):
#         if not lst:
#             return []
#         elif len(lst) == 1:
#             return [lst]

#         lst_permutations = []

#         for i in range(len(lst)):
#             m = lst[i]

#             remaining_lst = lst[:i] + lst[i+1:]

#             for p in self.permutations(remaining_lst):
#                 lst_permutations.append([m] + p)
        
#         return lst_permutations

#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """