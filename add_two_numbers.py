# https://leetcode.com/problems/add-two-numbers
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if other is None:
            return False
        return self.val == other.val and self.next == other.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """You are given two non-empty linked lists representing two non-negative integers.
            The digits are stored in reverse order, and each of their nodes contains a single digit.
            Add the two numbers and return the sum as a linked list."""
        head = tail = None
        carry = 0
        while l1 is not None or l2 is not None:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            l1 = l1 if l1 is None else l1.next
            l2 = l2 if l2 is None else l2.next

            carry = val // 10
            val %= 10

            if tail is not None:
                tail.next = ListNode(val)
                tail = tail.next
            else:
                head = tail = ListNode(val)

        if carry != 0:
            tail.next = ListNode(carry)
        return head


def test_1():
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    expected = ListNode(7, ListNode(0, ListNode(8)))
    assert Solution().addTwoNumbers(l1, l2) == expected


def test_2():
    l1 = ListNode(0)
    l2 = ListNode(0)
    expected = ListNode(0)
    assert Solution().addTwoNumbers(l1, l2) == expected


def test_3():
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    expected = ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))
    assert Solution().addTwoNumbers(l1, l2) == expected
