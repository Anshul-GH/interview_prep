'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1

 
Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is not None:
            # return depth
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)

            # use the larger length
            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1
        else:
            return 0

        # depth = 0
        # if (root is not None) or (root is not None and root.val == 0):
        #     depth += 1
        #     if root.left and root.right:
        #         depth -= 1
        #     if root.left:
        #         depth = depth + self.maxDepth(root.left)
        #     if root.right:
        #         depth = depth + self.maxDepth(root.right)

        # if root is not None:
        #     # return depth
        #     left_depth = maxDepth(root.left)
        #     right_depth = maxDepth(root.right)

        #     # use the larger length
        #     if left_depth > right_depth:
        #         return left_depth + 1
        #     else:
        #         return right_depth + 1
        # else:
        #     return 0
