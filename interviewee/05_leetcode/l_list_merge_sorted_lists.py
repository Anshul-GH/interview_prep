'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

 

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:        
            current_node1 = list1
            current_node2 = list2

            merged_list = ListNode()

            # assigning head to merged list
            if current_node1.val < current_node2.val:
                merged_list = ListNode(val=current_node1.val)    
                current_node1 = current_node1.next
                current_merged = merged_list
            else:
                merged_list = ListNode(val=current_node2.val) 
                current_node2 = current_node2.next
                current_merged = merged_list

            while current_node1 and current_node2:
                if current_node1.val < current_node2.val:
                    current_merged.next = current_node1
                    current_node1 = current_node1.next
                    current_merged = current_merged.next
                    current_merged.next = None
                else:
                    current_merged.next = current_node2
                    current_node2 = current_node2.next
                    current_merged = current_merged.next
                    current_merged.next = None

            while current_node1:
                current_merged.next = current_node1
                current_node1 = current_node1.next
                current_merged = current_merged.next
                current_merged.next = None

            while current_node2:
                current_merged.next = current_node2
                current_node2 = current_node2.next
                current_merged = current_merged.next
                current_merged.next = None
        elif list1:
            merged_list = list1
        else:
            merged_list = list2


        return merged_list
