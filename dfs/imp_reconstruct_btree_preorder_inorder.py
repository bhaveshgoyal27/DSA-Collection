class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_binary_tree(preorder: list[int], inorder: list[int]) -> Node:
    # WRITE YOUR BRILLIANT CODE HERE
    return None

def format_tree(node):
    if node is None:
        yield "x"
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)

if __name__ == "__main__":
    preorder = [int(x) for x in input().split()]
    inorder = [int(x) for x in input().split()]
    res = construct_binary_tree(preorder, inorder)
    print(" ".join(format_tree(res)))
