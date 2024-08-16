from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# https://leetcode.com/problems/linked-list-cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Given head, the head of a linked list, determine if the linked list has a cycle in it."""
        visited = []
        while head:
            if head in visited:
                return True
            visited.append(head)
            head = head.next
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        # if there is a cycle, slow and fast will meet at some point, and if there is no cycle, fast will reach the end.
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


def test_1():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    assert Solution().hasCycle(head) is True


def test_2():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    assert Solution().hasCycle(head) is True


def test_3():
    head = ListNode(1)
    assert Solution().hasCycle(head) is False
