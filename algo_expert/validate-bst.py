# https://www.algoexpert.io/questions/validate-bst
import sys


# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstRec(tree, -sys.maxsize, sys.maxsize)


def validateBstRec(tree: BST, father_left_val: int, father_right_val: int) -> bool:
    if not tree:
        return True
    if not father_left_val <= tree.value < father_right_val:
        return False
    return validateBstRec(tree.left, father_left_val, tree.value) and \
        validateBstRec(tree.right, tree.value, father_right_val)


def build_tree(nodes: list) -> BST:
    nodes_dict = {node['id']: BST(node['value']) for node in nodes}
    for node in nodes:
        if node['left']:
            nodes_dict[node['id']].left = nodes_dict[node['left']]
        if node['right']:
            nodes_dict[node['id']].right = nodes_dict[node['right']]
    return nodes_dict[nodes[0]['id']]


def test():
    tests = [{'tree': {'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10},
                                 {'id': '15', 'left': '13', 'right': '22', 'value': 15},
                                 {'id': '22', 'left': None, 'right': None, 'value': 22},
                                 {'id': '13', 'left': None, 'right': '14', 'value': 13},
                                 {'id': '14', 'left': None, 'right': None, 'value': 14},
                                 {'id': '5', 'left': '2', 'right': '5-2', 'value': 5},
                                 {'id': '5-2', 'left': None, 'right': None, 'value': 5},
                                 {'id': '2', 'left': '1', 'right': None, 'value': 2},
                                 {'id': '1', 'left': None, 'right': None, 'value': 1}],
                       'root': '10'}, 'expected': True},

             {'tree': {'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10},
                                 {'id': '15', 'left': None, 'right': '22', 'value': 15},
                                 {'id': '22', 'left': None, 'right': None, 'value': 22},
                                 {'id': '5', 'left': '2', 'right': '5-2', 'value': 5},
                                 {'id': '5-2', 'left': None, 'right': None, 'value': 5},
                                 {'id': '2', 'left': '1', 'right': None, 'value': 2},
                                 {'id': '1', 'left': '-5', 'right': None, 'value': 1},
                                 {'id': '-5', 'left': '-15', 'right': '-5-2', 'value': -5},
                                 {'id': '-5-2', 'left': None, 'right': '-2', 'value': -5},
                                 {'id': '-2', 'left': None, 'right': '-1', 'value': -2},
                                 {'id': '-1', 'left': None, 'right': None, 'value': -1},
                                 {'id': '-15', 'left': '-22', 'right': None, 'value': -15},
                                 {'id': '-22', 'left': None, 'right': None, 'value': -22}],
                       'root': '10'}, 'expected': True},

             {'tree': {'nodes': [{'id': '10', 'left': None, 'right': None, 'value': 10}],
                       'root': '10'}, 'expected': True},

             {'tree': {'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10},
                                 {'id': '15', 'left': None, 'right': '22', 'value': 15},
                                 {'id': '22', 'left': None, 'right': '500', 'value': 22},
                                 {'id': '500', 'left': '50', 'right': '1500', 'value': 500},
                                 {'id': '1500', 'left': None, 'right': '10000', 'value': 1500},
                                 {'id': '10000', 'left': '2200', 'right': None, 'value': 10000},
                                 {'id': '2200', 'left': None, 'right': None, 'value': 2200},
                                 {'id': '50', 'left': None, 'right': '200', 'value': 50},
                                 {'id': '200', 'left': None, 'right': None, 'value': 200},
                                 {'id': '5', 'left': '2', 'right': '5-2', 'value': 5},
                                 {'id': '5-2', 'left': None, 'right': None, 'value': 5},
                                 {'id': '2', 'left': '1', 'right': None, 'value': 2},
                                 {'id': '1', 'left': None, 'right': None, 'value': 1}],
                       'root': '10'}, 'expected': True},

             {'tree': {'nodes': [{'id': '5000', 'left': '5', 'right': '55000', 'value': 5000},
                                 {'id': '55000', 'left': None, 'right': None, 'value': 55000},
                                 {'id': '5', 'left': '2', 'right': '15', 'value': 5},
                                 {'id': '15', 'left': '5-2', 'right': '22', 'value': 15},
                                 {'id': '22', 'left': None, 'right': '502', 'value': 22},
                                 {'id': '502', 'left': '204', 'right': None, 'value': 502},
                                 {'id': '204', 'left': '203', 'right': '205', 'value': 204},
                                 {'id': '205', 'left': None, 'right': '207', 'value': 205},
                                 {'id': '207', 'left': '206', 'right': '208', 'value': 207},
                                 {'id': '208', 'left': None, 'right': None, 'value': 208},
                                 {'id': '206', 'left': None, 'right': None, 'value': 206},
                                 {'id': '203', 'left': None, 'right': None, 'value': 203},
                                 {'id': '5-2', 'left': None, 'right': None, 'value': 5},
                                 {'id': '2', 'left': '1', 'right': '3', 'value': 2},
                                 {'id': '3', 'left': None, 'right': None, 'value': 3},
                                 {'id': '1', 'left': None, 'right': '1-2', 'value': 1},
                                 {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1},
                                 {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1},
                                 {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1},
                                 {'id': '1-5', 'left': None, 'right': None, 'value': 1}],
                       'root': '5000'}, 'expected': True},

             {'tree': {'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10},
                                 {'id': '15', 'left': None, 'right': '22', 'value': 15},
                                 {'id': '22', 'left': None, 'right': None, 'value': 22},
                                 {'id': '5', 'left': '2', 'right': '5-2', 'value': 5},
                                 {'id': '5-2', 'left': None, 'right': '11', 'value': 5},
                                 {'id': '11', 'left': None, 'right': None, 'value': 11},
                                 {'id': '2', 'left': '1', 'right': None, 'value': 2},
                                 {'id': '1', 'left': None, 'right': None, 'value': 1}],
                       'root': '10'}, 'expected': False},

             {'tree': {'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10},
                                 {'id': '15', 'left': None, 'right': '22', 'value': 15},
                                 {'id': '22', 'left': None, 'right': None, 'value': 22},
                                 {'id': '5', 'left': '2', 'right': '5-2', 'value': 5},
                                 {'id': '5-2', 'left': None, 'right': None, 'value': 5},
                                 {'id': '2', 'left': '1', 'right': None, 'value': 2},
                                 {'id': '1', 'left': '-5', 'right': None, 'value': 1},
                                 {'id': '-5', 'left': '-15', 'right': '-5-2', 'value': -5},
                                 {'id': '-5-2', 'left': None, 'right': '-2', 'value': -5},
                                 {'id': '-2', 'left': None, 'right': '-1', 'value': -2},
                                 {'id': '-1', 'left': None, 'right': None, 'value': -1},
                                 {'id': '-15', 'left': '-22', 'right': None, 'value': -15},
                                 {'id': '-22', 'left': '11', 'right': None, 'value': -22},
                                 {'id': '11', 'left': None, 'right': None, 'value': 11}],
                       'root': '10'}, 'expected': False},

             {'tree': {'nodes': [{'id': '10', 'left': '11', 'right': '12', 'value': 10},
                                 {'id': '12', 'left': None, 'right': None, 'value': 12},
                                 {'id': '11', 'left': None, 'right': None, 'value': 11}],
                       'root': '10'}, 'expected': False},

             {'tree': {'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10},
                                 {'id': '15', 'left': None, 'right': '22', 'value': 15},
                                 {'id': '22', 'left': None, 'right': '500', 'value': 22},
                                 {'id': '500', 'left': '50', 'right': '1500', 'value': 500},
                                 {'id': '1500', 'left': None, 'right': '10000', 'value': 1500},
                                 {'id': '10000', 'left': '2200', 'right': '9999', 'value': 10000},
                                 {'id': '9999', 'left': None, 'right': None, 'value': 9999},
                                 {'id': '2200', 'left': None, 'right': None, 'value': 2200},
                                 {'id': '50', 'left': None, 'right': '200', 'value': 50},
                                 {'id': '200', 'left': None, 'right': None, 'value': 200},
                                 {'id': '5', 'left': '2', 'right': '5-2', 'value': 5},
                                 {'id': '5-2', 'left': None, 'right': None, 'value': 5},
                                 {'id': '2', 'left': '1', 'right': None, 'value': 2},
                                 {'id': '1', 'left': None, 'right': None, 'value': 1}],
                       'root': '10'}, 'expected': False},

             {'tree': {'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100},
                                 {'id': '502', 'left': '204', 'right': '55000', 'value': 502},
                                 {'id': '55000', 'left': None, 'right': None, 'value': 55000},
                                 {'id': '204', 'left': '203', 'right': '205', 'value': 204},
                                 {'id': '205', 'left': '300', 'right': '207', 'value': 205},
                                 {'id': '207', 'left': '206', 'right': '208', 'value': 207},
                                 {'id': '208', 'left': None, 'right': None, 'value': 208},
                                 {'id': '206', 'left': None, 'right': None, 'value': 206},
                                 {'id': '300', 'left': None, 'right': None, 'value': 300},
                                 {'id': '203', 'left': None, 'right': None, 'value': 203},
                                 {'id': '5', 'left': '2', 'right': '15', 'value': 5},
                                 {'id': '15', 'left': '5-2', 'right': '22', 'value': 15},
                                 {'id': '22', 'left': None, 'right': None, 'value': 22},
                                 {'id': '5-2', 'left': None, 'right': None, 'value': 5},
                                 {'id': '2', 'left': '1', 'right': '3', 'value': 2},
                                 {'id': '3', 'left': None, 'right': None, 'value': 3},
                                 {'id': '1', 'left': None, 'right': '1-2', 'value': 1},
                                 {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1},
                                 {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1},
                                 {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1},
                                 {'id': '1-5', 'left': None, 'right': None, 'value': 1}],
                       'root': '100'}, 'expected': False},

             {'tree': {'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10},
                                 {'id': '15', 'left': None, 'right': None, 'value': 15},
                                 {'id': '5', 'left': None, 'right': '10-2', 'value': 5},
                                 {'id': '10-2', 'left': None, 'right': None, 'value': 10}],
                       'root': '10'}, 'expected': False},

             {'tree': {'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10},
                                 {'id': '15', 'left': '13', 'right': '22', 'value': 15},
                                 {'id': '22', 'left': None, 'right': None, 'value': 22},
                                 {'id': '13', 'left': None, 'right': '16', 'value': 13},
                                 {'id': '16', 'left': None, 'right': None, 'value': 16},
                                 {'id': '5', 'left': '2', 'right': '5-2', 'value': 5},
                                 {'id': '5-2', 'left': None, 'right': None, 'value': 5},
                                 {'id': '2', 'left': '1', 'right': None, 'value': 2},
                                 {'id': '1', 'left': None, 'right': None, 'value': 1}],
                       'root': '10'}, 'expected': False},

             {'tree': {'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10},
                                 {'id': '15', 'left': '13', 'right': '22', 'value': 15},
                                 {'id': '22', 'left': None, 'right': None, 'value': 22},
                                 {'id': '13', 'left': None, 'right': '14', 'value': 5},
                                 {'id': '14', 'left': None, 'right': None, 'value': 14},
                                 {'id': '5', 'left': '2', 'right': '5-2', 'value': 5},
                                 {'id': '5-2', 'left': None, 'right': None, 'value': 5},
                                 {'id': '2', 'left': '1', 'right': None, 'value': 2},
                                 {'id': '1', 'left': None, 'right': None, 'value': 1}],
                       'root': '10'}, 'expected': False}]

    for test in tests:
        tree, expected = build_tree(test['tree']['nodes']), test['expected']
        assert validateBst(tree) == expected, f"expected {expected} for {test['tree']}"
