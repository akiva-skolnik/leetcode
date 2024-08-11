# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_list_bfs(self):
        q = [self]
        res = []
        while q:
            node = q.pop(0)
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)

        return res


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """Given an integer array nums where the elements are sorted in ascending order,
            convert it to a height-balanced binary search tree."""
        if not nums:
            return None
        mid = len(nums) // 2
        return TreeNode(val=nums[mid],
                        left=self.sortedArrayToBST(nums[:mid]),
                        right=self.sortedArrayToBST(nums[mid + 1:]))


# Test cases


def test_1():
    nums = [-10, -3, 0, 5, 9]
    expected = [0, -3, 9, -10, 5]
    assert Solution().sortedArrayToBST(nums).to_list_bfs() == expected


def test_2():
    nums = [1, 3]
    expected = [3, 1]
    assert Solution().sortedArrayToBST(nums).to_list_bfs() == expected
