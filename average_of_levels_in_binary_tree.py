from typing import List, Optional


# https://leetcode.com/problems/average-of-levels-in-binary-tree
class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """Given the root of a binary tree, return the average value of the nodes on each level"""
        result: list[(int, int)] = []

        def traverse_tree(root: Optional[TreeNode], level: int) -> None:
            if not root:
                return
            if len(result) == level:
                result.append((1, root.val))
            else:
                result[level] = (result[level][0] + 1, result[level][1] + root.val)
            traverse_tree(root.left, level + 1)
            traverse_tree(root.right, level + 1)

        traverse_tree(root, 0)
        return [s / n for (n, s) in result]


def test_1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().averageOfLevels(root) == [3.0, 14.5, 11.0]


def test_2():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(15)
    root.left.right = TreeNode(7)
    assert Solution().averageOfLevels(root) == [3.0, 14.5, 11.0]
