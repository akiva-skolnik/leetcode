from typing import Optional


# https://leetcode.com/problems/sort-list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Given the head of a linked list, return the list sorted in ascending order."""
        # a bit of cheating, but O(nlogn) solution. Note that it also works with more complex ListNode objects.
        if not head or not head.next:
            return head
        as_list = []
        while head:
            as_list.append(head)
            head = head.next
        as_list.sort(key=lambda x: x.val)
        as_list[-1].next = None
        as_list[-2].next = as_list[-1]
        for i in range(len(as_list) - 1):
            as_list[i].next = as_list[i + 1]
        return as_list[0]


def test_1():
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    sorted_head = Solution().sortList(head)
    assert sorted_head.val == 1


def test_2():
    head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    sorted_head = Solution().sortList(head)
    assert sorted_head.val == -1
    assert sorted_head.next.val == 0
    assert sorted_head.next.next.val == 3
    assert sorted_head.next.next.next.val == 4
    assert sorted_head.next.next.next.next.val == 5
    assert sorted_head.next.next.next.next.next is None


def test_3():
    assert Solution().sortList(None) is None


def test_object():
    head = ListNode(2, ListNode(1))
    sorted_head = Solution().sortList(head)
    assert sorted_head.next is head  # here we test not only the value but also the object
    assert sorted_head.next.next is None
