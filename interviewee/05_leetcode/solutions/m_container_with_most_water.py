# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        length = len(height)

        # for i in range(length):
        #     for j in range(i+1, length):
        #         area = max(area, min(height[j], height[i]) * (j - i))

        start = 0
        end = length - 1

        while start < end:
            curr_area = min(height[start], height[end]) * (end - start)
            max_area = max(max_area, curr_area)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area
