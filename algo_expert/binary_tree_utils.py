class BinaryTree:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


def build_tree(tree: dict) -> BinaryTree:
    nodes = {node['id']: BinaryTree(node['value']) for node in tree['nodes']}
    for node in tree['nodes']:
        if node['left']:
            nodes[node['id']].left = nodes[node['left']]
        if node['right']:
            nodes[node['id']].right = nodes[node['right']]
    return nodes[tree['root']]
