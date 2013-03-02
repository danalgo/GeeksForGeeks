"""
Print prime numbers between two ranges
The range must start from 2 till a number
"""

# Create linked-list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(start, end):
    if start > end:
        return None
    n = Node(start)
    n.next = create_linked_list(start+1, end)
    return n

def print_linked_list(head):
    if head is None:
        return
    print head.data,
    print_linked_list(head.next)

def find_primes(head):
    while head is not None:
        temp_head = head.next
        prev = head
        while temp_head is not None:
            if temp_head.data % head.data is 0:
                # Delete the temp_head_data node
                prev.next = temp_head.next
            else:
                prev = temp_head
            temp_head =temp_head.next
        head = head.next

if __name__=='__main__':
    head = create_linked_list(2,27)
    print_linked_list(head)

    find_primes(head)
    print ''
    print_linked_list(head)
