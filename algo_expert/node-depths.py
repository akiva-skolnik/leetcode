# https://www.algoexpert.io/questions/node-depths
from binary_tree_utils import BinaryTree, build_tree


def nodeDepths(root: BinaryTree, depth: int = 0) -> int:
    """returns the sum of the depths of all nodes in a binary tree"""
    if not root:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


def test():
    tests = [{'expected': 16,
              'tree': {'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1},
                                 {'id': '2', 'left': '4', 'right': '5', 'value': 2},
                                 {'id': '3', 'left': '6', 'right': '7', 'value': 3},
                                 {'id': '4', 'left': '8', 'right': '9', 'value': 4},
                                 {'id': '5', 'left': None, 'right': None, 'value': 5},
                                 {'id': '6', 'left': None, 'right': None, 'value': 6},
                                 {'id': '7', 'left': None, 'right': None, 'value': 7},
                                 {'id': '8', 'left': None, 'right': None, 'value': 8},
                                 {'id': '9', 'left': None, 'right': None, 'value': 9}],
                       'root': '1'}},

             {'expected': 0,
              'tree': {'nodes': [{'id': '1', 'left': None, 'right': None, 'value': 1}],
                       'root': '1'}},

             {'expected': 1,
              'tree': {'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1},
                                 {'id': '2', 'left': None, 'right': None, 'value': 2}],
                       'root': '1'}},

             {'expected': 2,
              'tree': {'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1},
                                 {'id': '2', 'left': None, 'right': None, 'value': 2},
                                 {'id': '3', 'left': None, 'right': None, 'value': 3}],
                       'root': '1'}},

             {'expected': 4,
              'tree': {'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1},
                                 {'id': '2', 'left': '4', 'right': None, 'value': 2},
                                 {'id': '3', 'left': None, 'right': None, 'value': 3},
                                 {'id': '4', 'left': None, 'right': None, 'value': 4}],
                       'root': '1'}},

             {'expected': 21,
              'tree': {'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1},
                                 {'id': '2', 'left': '3', 'right': None, 'value': 2},
                                 {'id': '3', 'left': '4', 'right': None, 'value': 3},
                                 {'id': '4', 'left': '5', 'right': None, 'value': 4},
                                 {'id': '5', 'left': '6', 'right': None, 'value': 5},
                                 {'id': '6', 'left': None, 'right': '7', 'value': 6},
                                 {'id': '7', 'left': None, 'right': None, 'value': 7}],
                       'root': '1'}},

             {'expected': 42,
              'tree': {'nodes': [{'id': '1', 'left': '2', 'right': '8', 'value': 1},
                                 {'id': '2', 'left': '3', 'right': None, 'value': 2},
                                 {'id': '3', 'left': '4', 'right': None, 'value': 3},
                                 {'id': '4', 'left': '5', 'right': None, 'value': 4},
                                 {'id': '5', 'left': '6', 'right': None, 'value': 5},
                                 {'id': '6', 'left': None, 'right': '7', 'value': 6},
                                 {'id': '7', 'left': None, 'right': None, 'value': 7},
                                 {'id': '8', 'left': None, 'right': '9', 'value': 8},
                                 {'id': '9', 'left': None, 'right': '10', 'value': 9},
                                 {'id': '10', 'left': None, 'right': '11', 'value': 10},
                                 {'id': '11', 'left': None, 'right': '12', 'value': 11},
                                 {'id': '12', 'left': '13', 'right': None, 'value': 12},
                                 {'id': '13', 'left': None, 'right': None, 'value': 13}],
                       'root': '1'}},

             {'expected': 51,
              'tree': {'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1},
                                 {'id': '2', 'left': '4', 'right': '5', 'value': 2},
                                 {'id': '3', 'left': '6', 'right': '7', 'value': 3},
                                 {'id': '4', 'left': '8', 'right': '9', 'value': 4},
                                 {'id': '5', 'left': None, 'right': None, 'value': 5},
                                 {'id': '6', 'left': '10', 'right': None, 'value': 6},
                                 {'id': '7', 'left': None, 'right': None, 'value': 7},
                                 {'id': '8', 'left': None, 'right': None, 'value': 8},
                                 {'id': '9', 'left': None, 'right': None, 'value': 9},
                                 {'id': '10', 'left': None, 'right': '11', 'value': 10},
                                 {'id': '11', 'left': '12', 'right': '13', 'value': 11},
                                 {'id': '12', 'left': '14', 'right': None, 'value': 12},
                                 {'id': '13', 'left': '15', 'right': '16', 'value': 13},
                                 {'id': '14', 'left': None, 'right': None, 'value': 14},
                                 {'id': '15', 'left': None, 'right': None, 'value': 15},
                                 {'id': '16', 'left': None, 'right': None, 'value': 16}],
                       'root': '1'}},

             {'expected': 36,
              'tree': {'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1},
                                 {'id': '2', 'left': '3', 'right': None, 'value': 2},
                                 {'id': '3', 'left': '4', 'right': None, 'value': 3},
                                 {'id': '4', 'left': '5', 'right': None, 'value': 4},
                                 {'id': '5', 'left': '6', 'right': None, 'value': 5},
                                 {'id': '6', 'left': '7', 'right': None, 'value': 6},
                                 {'id': '7', 'left': '8', 'right': None, 'value': 7},
                                 {'id': '8', 'left': '9', 'right': None, 'value': 8},
                                 {'id': '9', 'left': None, 'right': None, 'value': 9}],
                       'root': '1'}}]

    for test in tests:
        tree = build_tree(test['tree'])
        assert nodeDepths(tree) == test['expected']
