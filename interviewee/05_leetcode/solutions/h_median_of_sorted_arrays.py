# https://leetcode.com/problems/median-of-two-sorted-arrays/

import heapq

## Working: ChatGPT
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two sorted arrays
        merged_array = list(heapq.merge(nums1, nums2))

        # Get the length of the merged array
        n = len(merged_array)

        # If the length of the merged array is odd, return the middle element
        if n % 2 == 1:
            return merged_array[n // 2]

        # If the length of the merged array is even, return the average of the
        # two middle elements
        return (merged_array[n // 2 - 1] + merged_array[n // 2]) / 2

## Not Working
class Solution:
    def getMedian(self, lst):
        if len(lst)%2 == 1:
            median = lst[len(lst)//2]
        else:
            median = (lst[len(lst)//2-1]+lst[len(lst)//2])/2
        return median

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1:
            median1 = self.getMedian(nums1)
        else:
            median1 = None
        if nums2:
            median2 = self.getMedian(nums2)
        else:
            median2 = None
        
        consolidated = []
        if median1:
            consolidated.append(median1)
        if median2:
            consolidated.append(median2)

        if consolidated:
            median_result = self.getMedian(consolidated)
        else:
            median_result = 0

        return median_result