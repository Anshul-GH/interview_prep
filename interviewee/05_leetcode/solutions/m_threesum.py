# https://leetcode.com/problems/3sum/

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         solution = []
#         solution_set = []
#         sum = 0

#         for idx1,num1 in enumerate(nums):
#             rem_nums1 = nums[:idx1]+nums[idx1+1:]
#             for idx2,num2 in enumerate(rem_nums1):
#                 rem_nums2 = rem_nums1[:idx2]+rem_nums1[idx2+1:]
#                 rem_sum = sum - num1 - num2
#                 if rem_sum in rem_nums2:
#                     solution = [num1, num2, rem_sum]
#                     solution.sort()
#                     if solution not in solution_set:
#                         solution_set.append(solution)

#         return solution_set

# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()  # sort the array of numbers in ascending order
#         closest_sum = float('inf')  # set the closest sum to infinity
        
#         for i in range(len(nums) - 2):  # loop over the array (excluding the last two elements)
#             left = i + 1  # set the left pointer to the element next to the current element
#             right = len(nums) - 1  # set the right pointer to the last element in the array
            
#             while left < right:  # while the left pointer is less than the right pointer
#                 current_sum = nums[i] + nums[left] + nums[right]  # calculate the current sum
#                 if abs(target - current_sum) < abs(target - closest_sum):  # if the difference between the current sum and the target is less than the difference between the closest sum and the target
#                     closest_sum = current_sum  # update the closest sum
                
#                 if current_sum < target:  # if the current sum is less than the target
#                     left += 1  # increment the left pointer
#                 else:  # if the current sum is greater than or equal to the target
#                     right -= 1  # decrement the right pointer
        
#         return closest_sum  # return the closest sum


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         solution = []
#         solution_set = []
#         sum = 0

#         for idx1,num1 in enumerate(nums):
#             rem_nums1 = nums[:idx1]+nums[idx1+1:]
#             for idx2,num2 in enumerate(rem_nums1):
#                 rem_nums2 = rem_nums1[:idx2]+rem_nums1[idx2+1:]
#                 rem_sum = sum - num1 - num2
#                 if rem_sum in rem_nums2:
#                     solution = [num1, num2, rem_sum]
#                     solution.sort()
#                     if solution not in solution_set:
#                         solution_set.append(solution)

#         return solution_set

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     valid_triplets = []

    #     # iterate over all possible triplets
    #     len_nums = len(nums)
    #     for i in range(len_nums):
    #         for j in range(i+1, len_nums):
    #             for k in range(j+1, len_nums):
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     triplet = [nums[i], nums[j], nums[k]]
    #                     triplet.sort()
    #                     if triplet not in valid_triplets:
    #                         valid_triplets.append(triplet)
                        

    #     return list(valid_triplets)

        # Sort the array
        nums.sort()

        # Set to store the triplets
        triplets = set()

        # Iterate through the array, using the current number
        # as the first number in the triplet
        for i in range(len(nums)):
            # Skip over duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Use two pointers to search for the other two numbers
            # that sum to 0 with the current number
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # Calculate the sum of the three numbers
                sum = nums[i] + nums[left] + nums[right]

                # If the sum is 0, we have found a triplet
                if sum == 0:
                    # Add the triplet to the set of triplets
                    triplets.add((nums[i], nums[left], nums[right]))

                    # Skip over duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move the pointers inwards
                    left += 1
                    right -= 1
                elif sum < 0:
                    # If the sum is less than 0, we need to
                    # move the left pointer inwards to increase the sum
                    left += 1
                else:
                    # If the sum is greater than 0, we need to
                    # move the right pointer inwards to decrease the sum
                    right -= 1

        # Return the set of triplets as a list
        return list(triplets)

