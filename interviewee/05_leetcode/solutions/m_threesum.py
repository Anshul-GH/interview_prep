# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        solution_set = []
        sum = 0

        for idx1,num1 in enumerate(nums):
            rem_nums1 = nums[:idx1]+nums[idx1+1:]
            for idx2,num2 in enumerate(rem_nums1):
                rem_nums2 = rem_nums1[:idx2]+rem_nums1[idx2+1:]
                rem_sum = sum - num1 - num2
                if rem_sum in rem_nums2:
                    solution = [num1, num2, rem_sum]
                    solution.sort()
                    if solution not in solution_set:
                        solution_set.append(solution)

        return solution_set
