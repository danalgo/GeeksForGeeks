"""
Check if the given linked list is a palindrome 
using recursion.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(datas, index):
    if index is len(datas):
        return None
    head = Node(datas[index])
    head.next = create_linked_list(datas, index+1)
    return head

def print_linked_list(head):
    if head is None:
        return None
    print head.data,
    print_linked_list(head.next)

def center_node(head):
    temp = head
    length = 0
    isEven = False
    while head is not None:
        length+=1
        head = head.next
    if length%2 is 0:
        isEven = True
        length-=1
    for i in range(0,length/2):
        temp=temp.next 
    return temp, isEven

def is_palindrome(head, center, isEven):
    if head is center:
        if isEven:
            if center.data == center.next.data:
                return True, center.next.next
            else:
                return False, center.next.next
        else:
            return True, center.next
    else:
        status, future = is_palindrome(head.next, center, isEven)
        if status and future.data == head.data:
            return True, future.next
        else:
            return False, future.next
        
if __name__=='__main__':
    head = create_linked_list(list('ab'),0)
    print_linked_list(head)

    print ''
    center, isEven = center_node(head)
    print 'Center node data', center.data

    print 'Is it a palindrome: ', is_palindrome(head, center, isEven)
