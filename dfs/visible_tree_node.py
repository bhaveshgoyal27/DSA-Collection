class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    if not root:
        return 0

    def dfs(root, max_val):
        if not root:
            return 0
        op = 0
        if root.val>=max_val:
            max_val = root.val
            op = 1
        op += dfs(root.left, max_val)+ dfs(root.right, max_val)

        return op

    return dfs(root, float("-inf"))
    # WRITE YOUR BRILLIANT CODE HERE

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
    res = visible_tree_node(root)
    print(res)
