# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Notice that you may not slant the container.

# Example:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water the container can contain is 49.

# my solution (not working)
# def max_area_container(arr):
#     left = 0
#     right = len(arr)-1
#     max_area = 0

#     while left < right:
#         len_x = right - left
#         len_y = min(arr[left], arr[right])

#         area = len_x * len_y

#         max_area = max(max_area, area)

#         if (arr[left+1] - arr[left]) >= (arr[right-1] - arr[right]):
#             left += 1
#         else:
#             right -= 1

#     return max_area

# working solution
def max_area_container(height):
    maxarea = 0
    l = 0
    r = len(height)-1

    while(l<r):
        maxarea = max(maxarea, min(height[l],height[r])*(r-l))
        if(height[l]<height[r]):
            l+=1
        else:
            r-=1
    return maxarea


if __name__ == '__main__':
    my_arr = [1,8,6,2,5,4,8,25,7]
    # [1,2,4,3]
    # [1,8,6,2,5,4,8,3,7]
    max_area = max_area_container(my_arr)

    print(max_area)
