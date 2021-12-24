'''
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9
 
Follow up: Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # traverse and collect l_list data into a list
        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        if len(lst) % 2 == 0:
            mid = len(lst)//2
            if lst[:mid] == lst[mid:][::-1]:
                return True
            else:
                return False
        else:
            mid = len(lst)//2
            if lst[:mid] == lst[mid+1:][::-1]:
                return True
            else:
                return False
