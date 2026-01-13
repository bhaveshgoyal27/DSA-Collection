class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> list[list[int]]:
    from collections import deque

    if not root:
        return []

    d = deque()
    d.append(root)
    d.append(None)
    cur_level = 0
    cur_level_ele = []
    ans = []
    while len(d) > 0:
        val = d.popleft()
        if not val:
            cur_level += 1
            ans.append(cur_level_ele)
            cur_level_ele = []

            if len(d) > 0:
                d.append(None)

            continue

        cur_level_ele.append(val.val)
        if val.left:
            d.append(val.left)
        if val.right:
            d.append(val.right)

    return ans

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
    res = level_order_traversal(root)
    for row in res:
        print(" ".join(map(str, row)))
