class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth1(root: Node) -> int:
    if not root:
        return 0
    left_depth = tree_max_depth1(root.left)
    right_depth = tree_max_depth1(root.right)
    return max(left_depth, right_depth)+1
    # WRITE YOUR BRILLIANT CODE HERE

def tree_max_depth(root: Node) -> int:
    a = tree_max_depth1(root)
    if a:
        return a-1
    return a

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == "__main__":
    root = build_tree(iter(input().split()), int)
    res = tree_max_depth(root)
    print(res)
