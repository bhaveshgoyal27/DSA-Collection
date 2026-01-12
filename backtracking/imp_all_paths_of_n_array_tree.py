class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> list[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    if not root:
        return []
    res =[]
    path = []
    def traverse(node, path):
        path.append(str(node.val))
        if not node.children:
            res.append("->".join(path))
        else:
            for ch in node.children:
                traverse(ch, path)
        path.pop()

    traverse(root, path)
    return res