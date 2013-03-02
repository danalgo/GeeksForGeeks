"""
Reversing a linked-list using recursion
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(head):
    """Print linked-list"""
    if head is None:
        return
    print head.data,
    print_linked_list(head.next)

def create_sample_linked_list(start, end):
    """Create linked-list"""
    if start > end:
        return None
    n = Node(start)
    n.next = create_sample_linked_list(start+1,end)
    return n

def reverse_recursion(prev, curr):
    """Reversing the linked-list"""
    if curr is None:
        return prev
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
    return reverse_recursion(prev, curr)

if __name__ == '__main__':
    head = create_sample_linked_list(1,25)
    print_linked_list(head)

    print ''
    rev_head = reverse_recursion(None, head)
    print_linked_list(rev_head)
