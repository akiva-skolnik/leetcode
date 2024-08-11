from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l3 = None
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                val = l2.val
                l2 = l2.next

            elif l2 is None:
                val = l1.val
                l1 = l1.next

            else:
                val = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next

            val += carry
            carry = 0
            if val > 9:
                carry = val // 10
                val %= 10

            if l3 is not None:
                l3.next = l3 = ListNode(val)
            else:
                head = l3 = ListNode(val)

        if carry != 0:
            l3.next = ListNode(carry)
        return head
