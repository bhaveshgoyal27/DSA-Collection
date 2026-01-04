class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = slow = fast = head

    for i in range(n):
        if fast.next:
            fast = fast.next
        else:
            break

    if fast == None:
        head = head.next
        return head

    while fast.next:
        slow = slow.next
        fast = fast.next
    if slow == dummy:
        head = head.next
        return head
    else:
        if slow is None:
            return head
        else:
            dummy = slow.next
            slow.next = dummy.next
    return head
