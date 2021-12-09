'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz


Follow up: Could you do this in one pass?
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        current_node = head

        while current_node.next is not None:
            current_node = current_node.next
            counter += 1
        
        position = counter - n
        count = 0
        previous_node = head
        current_node = head

        while count <= position:
            previous_node = current_node
            current_node = current_node.next
            count += 1
        
        previous_node.next = current_node.next

        return head
