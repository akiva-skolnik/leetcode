from typing import Optional


# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B
            where V = |A.val - B.val| and A is an ancestor of B."""
        if not root:
            return 0
        return self.maxDiffRec(root, root.val, root.val)

    def maxDiffRec(self, root: Optional[TreeNode], curr_min: int, curr_max: int) -> int:
        if not root:
            return curr_max - curr_min
        curr_min = min(curr_min, root.val)
        curr_max = max(curr_max, root.val)
        return max(self.maxDiffRec(root.right, curr_min, curr_max),
                   self.maxDiffRec(root.left, curr_min, curr_max))


def test_1():
    root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
                    TreeNode(10, None, TreeNode(14, TreeNode(13))))
    assert Solution().maxAncestorDiff(root) == 7


def test_2():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(0, TreeNode(3))))
    assert Solution().maxAncestorDiff(root) == 3
