import math

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

MAX_EDGE = 1000000

def find_max_edge(root, ssum):
   global MAX_EDGE

   if root is None:
       return 0
   sum_left = find_max_edge(root.left, ssum)
   sum_right = find_max_edge(root.right, ssum)

   ssum_node = sum_left + sum_right + root.data
   MAX_EDGE = min( int(math.fabs(ssum - 2*ssum_node)), MAX_EDGE)
   return ssum_node

def ssum_tree(root):
    if root is None:
        return 0
    l = ssum_tree(root.left)
    r = ssum_tree(root.right)
    return l + r + root.data

if __name__=='__main__':
    root = Node(1)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)
    root.left.left.right = Node(9)

    ssum = ssum_tree(root)

    #find_max_edge(root.left, ssum)
    find_max_edge(root.right, ssum)
    print MAX_EDGE
