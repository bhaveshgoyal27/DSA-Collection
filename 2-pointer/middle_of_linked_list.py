class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head: Node) -> int:
    slow = fast=head
    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next

    return slow.val
    # WRITE YOUR BRILLIANT CODE HERE
    return 0