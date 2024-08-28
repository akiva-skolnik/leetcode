from typing import Optional


# https://leetcode.com/problems/merge-two-sorted-lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


def test_1():
    # 1 -> 1 -> 2 -> 3 -> 4 -> 4
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    merged = Solution().mergeTwoLists(l1, l2)
    assert merged.val == 1
    assert merged.next.val == 1
    assert merged.next.next.val == 2
    assert merged.next.next.next.val == 3
    assert merged.next.next.next.next.val == 4
    assert merged.next.next.next.next.next.val == 4


def test_2():
    assert Solution().mergeTwoLists(None, None) is None


def test_3():
    assert Solution().mergeTwoLists(None, ListNode(0)).val == ListNode(0).val


def test_4():
    # 1 -> 2 -> 4
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = None

    merged = Solution().mergeTwoLists(l1, l2)
    assert merged.val == 1
    assert merged.next.val == 2
    assert merged.next.next.val == 4
