from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# https://leetcode.com/problems/linked-list-cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        while head:
            if head in visited:
                return True
            visited.append(head)
            head = head.next
        return False



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
