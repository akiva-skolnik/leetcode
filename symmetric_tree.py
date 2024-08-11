# https://leetcode.com/problems/symmetric-tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Given the root of a binary tree, check whether it is a mirror of itself
            (i.e., symmetric around its center)."""
        def is_2_trees_mirror(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val != root2.val:
                return False
            return is_2_trees_mirror(root1.left, root2.right) and \
                is_2_trees_mirror(root1.right, root2.left)

        return not root or is_2_trees_mirror(root.left, root.right)


def test_1():
    root = TreeNode(1,
                    TreeNode(2, TreeNode(3), TreeNode(4)),
                    TreeNode(2, TreeNode(4), TreeNode(3))
                    )
    assert Solution().isSymmetric(root) is True

def test_2():
    root = TreeNode(1,
                    TreeNode(2, None, TreeNode(3)),
                    TreeNode(2, None, TreeNode(3))
                    )
    assert Solution().isSymmetric(root) is False