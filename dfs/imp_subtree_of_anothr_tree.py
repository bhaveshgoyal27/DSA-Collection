class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def subtree_of_another_tree(root: Node, sub_root: Node) -> bool:
    if not root and not sub_root:
        return False
    if not root:
        return not sub_root

    def dfs(root, sub_root):
        if not root:
            return not sub_root

        if not sub_root:
            return False

        if root.val != sub_root.val:
            return False

        return dfs(root.left, sub_root.left) and dfs(root.right, sub_root.right)

    if root.val == sub_root.val and dfs(root, sub_root):
        return True

    return subtree_of_another_tree(root.left, sub_root) or subtree_of_another_tree(root.right, sub_root)

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
    sub_root = build_tree(iter(input().split()), int)
    res = subtree_of_another_tree(root, sub_root)
    print("true" if res else "false")
