'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
'''
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # base case
        if not root:
            return []
        
        # create an empty queue and add the root node to it
        queue = deque()
        queue.append(root)

        level_data = {}
        level = 0

        # loop till queue is empty
        while queue:
            # process each node in the queue and enqueue
            # their non empty left and right childs
            curr = queue.popleft()

            if level in level_data:
                level_data[level].append(curr.val)
            else:
                level_data[level] = [curr.val]

            if curr.left and curr.right:
                level += 1
                queue.append(curr.left)
                queue.append(curr.right)

            elif curr.left and not curr.right:
                level += 1
                queue.append(curr.left)

            elif curr.right and not curr.left:
                level += 1
                queue.append(curr.right)

        # return level_data

        output = []
        for lst in level_data.values():
            output.append(lst)

        return output



    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     ord_list = []
    #     ht = self.get_tree_height(root)
    #     for i in range(1, ht+1):
    #         ord_list.append(self.get_current_level(root, i))

    #     return ord_list

    # def get_tree_height(self, root):
    #     if root is None:
    #         return 0
    #     else:
    #         lheight = self.get_tree_height(root.left)
    #         rheight = self.get_tree_height(root.right)
        
    #     # use the larger of the two height
    #     if lheight > rheight:
    #         return lheight + 1
    #     else:
    #         return rheight + 1
    
    # def get_current_level(self, root, level):
    #     if root is None:
    #         return None
        
    #     if level == 1:
    #         return [root.val]
    #     elif level > 1:
    #         return self.get_current_level(root.left, level-1) and \
    #             self.get_current_level(root.right, level-1)

