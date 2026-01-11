class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(tree: Node) -> bool:
    def check_tree(tree):
        if not tree:
            return 0
        left_height = check_tree(tree.left)
        right_height = check_tree(tree.right)

        if left_height==-1 or right_height == -1:
            return -1
        if abs(left_height-right_height)>1:
            return -1
        return max(left_height, right_height)+1
    res = check_tree(tree)
    if res==-1:
        return False
    # WRITE YOUR BRILLIANT CODE HERE
    return True

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
    tree = build_tree(iter(input().split()), int)
    res = is_balanced(tree)
    print("true" if res else "false")
