# https://www.algoexpert.io/questions/remove-duplicates-from-linked-list
class LinkedList:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

    def to_nodes_list(self):
        nodes = []
        node = self
        while node:
            nodes.append({'id': str(node.value), 'value': node.value,
                          'next': str(node.next.value) if node.next else None})
            node = node.next
        return nodes


def removeDuplicatesFromLinkedList(linkedList: LinkedList) -> LinkedList:
    prv = linkedList
    node = linkedList.next
    while node:
        if node.value == prv.value:
            prv.next = node.next
        else:
            prv = prv.next
        node = node.next
    return linkedList


def build_linked_list(data):
    nodes = {}
    for node in data['nodes']:
        nodes[node['id']] = LinkedList(node['value'])
    for node in data['nodes']:
        if node['next']:
            nodes[node['id']].next = nodes[node['next']]
    return nodes[data['head']]


def test():
    tests = [{'expected': [{'id': '1', 'next': '3', 'value': 1},
                           {'id': '3', 'next': '4', 'value': 3},
                           {'id': '4', 'next': '5', 'value': 4},
                           {'id': '5', 'next': '6', 'value': 5},
                           {'id': '6', 'next': None, 'value': 6}],
              'linkedList': {'head': '1',
                             'nodes': [{'id': '1', 'next': '1-2', 'value': 1},
                                       {'id': '1-2', 'next': '1-3', 'value': 1},
                                       {'id': '1-3', 'next': '2', 'value': 1},
                                       {'id': '2', 'next': '3', 'value': 3},
                                       {'id': '3', 'next': '3-2', 'value': 4},
                                       {'id': '3-2', 'next': '3-3', 'value': 4},
                                       {'id': '3-3', 'next': '4', 'value': 4},
                                       {'id': '4', 'next': '5', 'value': 5},
                                       {'id': '5', 'next': '5-2', 'value': 6},
                                       {'id': '5-2', 'next': None, 'value': 6}]}},
             {'expected': [{'id': '1', 'next': '4', 'value': 1},
                           {'id': '4', 'next': '5', 'value': 4},
                           {'id': '5', 'next': '6', 'value': 5},
                           {'id': '6', 'next': None, 'value': 6}],
              'linkedList': {'head': '1',
                             'nodes': [{'id': '1', 'next': '1-2', 'value': 1},
                                       {'id': '1-2', 'next': '1-3', 'value': 1},
                                       {'id': '1-3', 'next': '1-4', 'value': 1},
                                       {'id': '1-4', 'next': '1-5', 'value': 1},
                                       {'id': '1-5', 'next': '4', 'value': 1},
                                       {'id': '4', 'next': '4-2', 'value': 4},
                                       {'id': '4-2', 'next': '5', 'value': 4},
                                       {'id': '5', 'next': '6', 'value': 5},
                                       {'id': '6', 'next': '6-2', 'value': 6},
                                       {'id': '6-2', 'next': None, 'value': 6}]}},
             {'expected': [{'id': '1', 'next': None, 'value': 1}],
              'linkedList': {'head': '1',
                             'nodes': [{'id': '1', 'next': '1-2', 'value': 1},
                                       {'id': '1-2', 'next': '1-3', 'value': 1},
                                       {'id': '1-3', 'next': '1-4', 'value': 1},
                                       {'id': '1-4', 'next': '1-5', 'value': 1},
                                       {'id': '1-5', 'next': '1-6', 'value': 1},
                                       {'id': '1-6', 'next': '1-7', 'value': 1},
                                       {'id': '1-7', 'next': None, 'value': 1}]}},
             {'expected': [{'id': '1', 'next': '9', 'value': 1},
                           {'id': '9', 'next': '11', 'value': 9},
                           {'id': '11', 'next': '15', 'value': 11},
                           {'id': '15', 'next': '16', 'value': 15},
                           {'id': '16', 'next': '17', 'value': 16},
                           {'id': '17', 'next': None, 'value': 17}],
              'linkedList': {'head': '1',
                             'nodes': [{'id': '1', 'next': '9', 'value': 1},
                                       {'id': '9', 'next': '11', 'value': 9},
                                       {'id': '11', 'next': '15', 'value': 11},
                                       {'id': '15', 'next': '15-2', 'value': 15},
                                       {'id': '15-2', 'next': '16', 'value': 15},
                                       {'id': '16', 'next': '17', 'value': 16},
                                       {'id': '17', 'next': None, 'value': 17}]}},
             {'expected': [{'id': '1', 'next': None, 'value': 1}],
              'linkedList': {'head': '1',
                             'nodes': [{'id': '1', 'next': None, 'value': 1}]}},
             {'expected': [{'id': '-5', 'next': '-1', 'value': -5},
                           {'id': '-1', 'next': '5', 'value': -1},
                           {'id': '5', 'next': '8', 'value': 5},
                           {'id': '8', 'next': '9', 'value': 8},
                           {'id': '9', 'next': '10', 'value': 9},
                           {'id': '10', 'next': '11', 'value': 10},
                           {'id': '11', 'next': None, 'value': 11}],
              'linkedList': {'head': '-5',
                             'nodes': [{'id': '-5', 'next': '-1', 'value': -5},
                                       {'id': '-1', 'next': '-1-2', 'value': -1},
                                       {'id': '-1-2', 'next': '-1-3', 'value': -1},
                                       {'id': '-1-3', 'next': '5', 'value': -1},
                                       {'id': '5', 'next': '5-2', 'value': 5},
                                       {'id': '5-2', 'next': '5-3', 'value': 5},
                                       {'id': '5-3', 'next': '8', 'value': 5},
                                       {'id': '8', 'next': '8-2', 'value': 8},
                                       {'id': '8-2', 'next': '9', 'value': 8},
                                       {'id': '9', 'next': '10', 'value': 9},
                                       {'id': '10', 'next': '11', 'value': 10},
                                       {'id': '11', 'next': '11-2', 'value': 11},
                                       {'id': '11-2', 'next': None, 'value': 11}]}},
             {'expected': [{'id': '1', 'next': '2', 'value': 1},
                           {'id': '2', 'next': '3', 'value': 2},
                           {'id': '3', 'next': '4', 'value': 3},
                           {'id': '4', 'next': '5', 'value': 4},
                           {'id': '5', 'next': '6', 'value': 5},
                           {'id': '6', 'next': '7', 'value': 6},
                           {'id': '7', 'next': '8', 'value': 7},
                           {'id': '8', 'next': '9', 'value': 8},
                           {'id': '9', 'next': '10', 'value': 9},
                           {'id': '10', 'next': '11', 'value': 10},
                           {'id': '11', 'next': '12', 'value': 11},
                           {'id': '12', 'next': None, 'value': 12}],
              'linkedList': {'head': '1',
                             'nodes': [{'id': '1', 'next': '2', 'value': 1},
                                       {'id': '2', 'next': '3', 'value': 2},
                                       {'id': '3', 'next': '4', 'value': 3},
                                       {'id': '4', 'next': '5', 'value': 4},
                                       {'id': '5', 'next': '6', 'value': 5},
                                       {'id': '6', 'next': '7', 'value': 6},
                                       {'id': '7', 'next': '8', 'value': 7},
                                       {'id': '8', 'next': '9', 'value': 8},
                                       {'id': '9', 'next': '10', 'value': 9},
                                       {'id': '10', 'next': '11', 'value': 10},
                                       {'id': '11', 'next': '12', 'value': 11},
                                       {'id': '12', 'next': '12-2', 'value': 12},
                                       {'id': '12-2', 'next': None, 'value': 12}]}}]

    for i, test in enumerate(tests):
        got = removeDuplicatesFromLinkedList(build_linked_list(test['linkedList']))
        got = got.to_nodes_list()
        assert got == test['expected'], f"Test case {i} failed: got({got}), expected({test['expected']})"
