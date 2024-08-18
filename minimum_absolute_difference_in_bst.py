from typing import Optional


# https://leetcode.com/problems/minimum-absolute-difference-in-bst
class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prv_val: Optional[int] = None
        min_abs: Optional[int] = None

        def in_order(root: Optional[TreeNode]) -> None:
            nonlocal prv_val, min_abs
            if not root:
                return
            in_order(root.left)

            if prv_val is not None:
                if min_abs is None:
                    min_abs = abs(prv_val - root.val)
                else:
                    min_abs = min(min_abs, abs(prv_val - root.val))
            prv_val = root.val

            in_order(root.right)

        in_order(root)
        return min_abs


def test_1():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    assert Solution().getMinimumDifference(root) == 1


def test_2():
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    assert Solution().getMinimumDifference(root) == 1
