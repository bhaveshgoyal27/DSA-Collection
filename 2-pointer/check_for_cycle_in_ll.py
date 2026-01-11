def has_cycle(nodes: """Node""") -> bool:
    slow = fast = nodes
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            return True
    # WRITE YOUR BRILLIANT CODE HERE
    return False