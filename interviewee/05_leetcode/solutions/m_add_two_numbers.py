# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_digits(self, n1, n2, carry):
        addn = n1 + n2 + carry
        carry = int(addn//10)
        addn = addn % 10

        return addn, carry

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        addn = 0
        result = ListNode()

        traverse_l1 = l1
        traverse_l2 = l2
        traverse_result = result

        while traverse_l1 and traverse_l2:
            addn, carry = self.add_two_digits(traverse_l1.val, traverse_l2.val, carry)
            traverse_result.val = addn
            if traverse_l1.next or traverse_l2.next:
                traverse_result.next = ListNode()
            elif carry > 0:
                traverse_result.next = ListNode(carry)
            else:
                traverse_result.next = None
            traverse_l1 = traverse_l1.next
            traverse_l2 = traverse_l2.next
            traverse_result = traverse_result.next
    

        if traverse_l2 and not traverse_l1:
            while traverse_l2:
                addn, carry = self.add_two_digits(0, traverse_l2.val, carry)
                traverse_result.val = addn
                if traverse_l2.next:
                    traverse_result.next = ListNode()
                elif carry > 0:
                    traverse_result.next = ListNode(carry)
                else:
                    traverse_result.next = None
                traverse_l2 = traverse_l2.next
                traverse_result = traverse_result.next
        elif traverse_l1 and not traverse_l2:
            while traverse_l1:
                addn, carry = self.add_two_digits(traverse_l1.val, 0, carry)
                traverse_result.val = addn
                if traverse_l1.next:
                    traverse_result.next = ListNode()
                elif carry > 0:
                    traverse_result.next = ListNode(carry)
                else:
                    traverse_result.next = None
                traverse_l1 = traverse_l1.next
                traverse_result = traverse_result.next

        # if not traverse_l1 and not traverse_l2 and carry > 0:    
        #     traverse_result = ListNode(carry)

        return result
