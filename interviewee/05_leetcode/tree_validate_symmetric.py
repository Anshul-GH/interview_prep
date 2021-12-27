'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100
 
Follow up: Could you solve it both recursively and iteratively?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetricUtils(self, root1, root2):
        # both the roots are none/empty trees
        if not root1 and not root2:
            return True
        
        if root1 and root2:
            if root1.val == root2.val:
                return (self.isSymmetricUtils(root1.left, root2.right) and \
                    self.isSymmetricUtils(root1.right, root2.left))
        
        return False
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.isSymmetricUtils(root, root)
