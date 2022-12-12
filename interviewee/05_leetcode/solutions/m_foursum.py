# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        len_nums = len(nums)

        for i in range(len_nums):
            for j in range(i+1, len_nums):
                for k in range(j+1, len_nums):
                    for l in range(k+1, len_nums):
                        if nums[i]+nums[j]+nums[k]+nums[l] == target:
                            quad = [nums[i], nums[j], nums[k], nums[l]]
                            quad.sort()
                            if quad not in output:
                                output.append(quad)
        return output
