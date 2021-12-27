'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    -2^31 <= Node.val <= 2^31 - 1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBSTUtil(self, node, maxm=(2**32-1), minm=(-2**32)):
        if node is None:
            return True
        
        if node.val < minm or node.val > maxm:
            return False
            
        return (self.isValidBSTUtil(node.left, maxm=(node.val-1), minm=minm) \
            and self.isValidBSTUtil(node.right, maxm=maxm, minm=(node.val+1)))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTUtil(root)

#         if root:
#             is_valid = True
#             if root.left:
#                 if root.left.val < root.val:                    
#                     is_valid = self.isValidBST(root.left)
#                 else:
#                     is_valid = False
#             if root.right:
#                 if root.right.val > root.val:                    
#                     is_valid = self.isValidBST(root.right)
#                 else:
#                     is_valid = False
            
#             return is_valid
#         else:
#             return True
