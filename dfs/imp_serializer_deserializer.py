class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return "x"

    current = f"{root.val}"
    current += " " + serialize(root.left)
    current += " " + serialize(root.right)
    return current

def deserialize(s):
    lst = s.split(" ")
    def builder(node):
        val = next(node)
        if not val or val == "x":
            return None
        cur = Node(val)
        cur.left = builder(node)
        cur.right = builder(node)
        return cur
    return builder(iter(lst))


if __name__ == "__main__":
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == "x":
            return None
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur

    def print_tree(root):
        if not root:
            yield "x"
            return
        yield str(root.val)
        yield from print_tree(root.left)
        yield from print_tree(root.right)

    root = build_tree(iter(input().split()))
    new_root = deserialize(serialize(root))
    print(" ".join(print_tree(new_root)))
