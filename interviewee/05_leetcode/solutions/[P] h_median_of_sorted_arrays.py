# https://leetcode.com/problems/median-of-two-sorted-arrays/

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