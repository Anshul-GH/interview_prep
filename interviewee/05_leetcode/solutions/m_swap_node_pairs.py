# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val != current.next.val:
                current.val, current.next.val = current.next.val, current.val
            
            current = current.next.next

        return head
