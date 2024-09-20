# https://www.algoexpert.io/questions/branch-sums

class BinaryTree:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


def branchSums(root: BinaryTree, s: int = 0) -> list:
    if not root:
        return []
    s += root.value
    if not root.right and not root.left:
        return [s]
    return branchSums(root.left, s) + branchSums(root.right, s)


def build_tree(tree: dict) -> BinaryTree:
    nodes = {node['id']: BinaryTree(node['value']) for node in tree['nodes']}
    for node in tree['nodes']:
        if node['left']:
            nodes[node['id']].left = nodes[node['left']]
        if node['right']:
            nodes[node['id']].right = nodes[node['right']]
    return nodes[tree['root']]


def test():
    tests = [{'tree': {'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1},
                                 {'id': '2', 'left': '4', 'right': '5', 'value': 2},
                                 {'id': '3', 'left': '6', 'right': '7', 'value': 3},
                                 {'id': '4', 'left': '8', 'right': '9', 'value': 4},
                                 {'id': '5', 'left': '10', 'right': None, 'value': 5},
                                 {'id': '6', 'left': None, 'right': None, 'value': 6},
                                 {'id': '7', 'left': None, 'right': None, 'value': 7},
                                 {'id': '8', 'left': None, 'right': None, 'value': 8},
                                 {'id': '9', 'left': None, 'right': None, 'value': 9},
                                 {'id': '10', 'left': None, 'right': None, 'value': 10}],
                       'root': '1'}, 'expected': [15, 16, 18, 10, 11]},

             {'tree': {'nodes': [{'id': '1', 'left': None, 'right': None, 'value': 1}],
                       'root': '1'}, 'expected': [1]},

             {'tree': {'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1},
                                 {'id': '2', 'left': None, 'right': None, 'value': 2}],
                       'root': '1'}, 'expected': [3]},

             {'tree': {'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1},
                                 {'id': '2', 'left': None, 'right': None, 'value': 2},
                                 {'id': '3', 'left': None, 'right': None, 'value': 3}],
                       'root': '1'}, 'expected': [3, 4]},

             {'tree': {'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1},
                                 {'id': '2', 'left': '4', 'right': '5', 'value': 2},
                                 {'id': '3', 'left': None, 'right': None, 'value': 3},
                                 {'id': '4', 'left': None, 'right': None, 'value': 4},
                                 {'id': '5', 'left': None, 'right': None, 'value': 5}],
                       'root': '1'}, 'expected': [7, 8, 4]},

             {'tree': {'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1},
                                 {'id': '2', 'left': '4', 'right': '5', 'value': 2},
                                 {'id': '3', 'left': '6', 'right': '7', 'value': 3},
                                 {'id': '4', 'left': '8', 'right': '9', 'value': 4},
                                 {'id': '5', 'left': '10', 'right': '1-2', 'value': 5},
                                 {'id': '6', 'left': '1-3', 'right': '1-4', 'value': 6},
                                 {'id': '7', 'left': None, 'right': None, 'value': 7},
                                 {'id': '8', 'left': None, 'right': None, 'value': 8},
                                 {'id': '9', 'left': None, 'right': None, 'value': 9},
                                 {'id': '10', 'left': None, 'right': None, 'value': 10},
                                 {'id': '1-2', 'left': None, 'right': None, 'value': 1},
                                 {'id': '1-3', 'left': None, 'right': None, 'value': 1},
                                 {'id': '1-4', 'left': None, 'right': None, 'value': 1}],
                       'root': '1'}, 'expected': [15, 16, 18, 9, 11, 11, 11]},

             {'tree': {'nodes': [{'id': '0', 'left': '1', 'right': None, 'value': 0},
                                 {'id': '1', 'left': '10', 'right': None, 'value': 1},
                                 {'id': '10', 'left': '100', 'right': None, 'value': 10},
                                 {'id': '100', 'left': None, 'right': None, 'value': 100}],
                       'root': '0'}, 'expected': [111]},

             {'tree': {'nodes': [{'id': '0', 'left': None, 'right': '1', 'value': 0},
                                 {'id': '1', 'left': None, 'right': '10', 'value': 1},
                                 {'id': '10', 'left': None, 'right': '100', 'value': 10},
                                 {'id': '100', 'left': None, 'right': None, 'value': 100}],
                       'root': '0'}, 'expected': [111]},

             {'tree': {'nodes': [{'id': '0', 'left': '9', 'right': '1', 'value': 0},
                                 {'id': '9', 'left': None, 'right': None, 'value': 9},
                                 {'id': '1', 'left': '15', 'right': '10', 'value': 1},
                                 {'id': '15', 'left': None, 'right': None, 'value': 15},
                                 {'id': '10', 'left': '100', 'right': '200', 'value': 10},
                                 {'id': '100', 'left': None, 'right': None, 'value': 100},
                                 {'id': '200', 'left': None, 'right': None, 'value': 200}],
                       'root': '0'}, 'expected': [9, 16, 111, 211]}]

    for test in tests:
        tree = build_tree(test['tree'])
        result = branchSums(tree)
        assert result == test['expected'], f"expected {test['expected']} but got {result}"
