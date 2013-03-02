"""
The diameter of a tree is the number of nodes on the longest path between two leaves in he tree
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def create_tree():
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('h')
    root.left.left.left = Node('e')

    return root

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print root.data,
    inorder(root.right)

def height(root):
    if root is None:
        return 0
    return max( height(root.left),
                height(root.right)) +1

def diameter(root):
    if root is None:
        return 0
    ldiamter = dimater(root.left)
    rdiamter = dimater(root.right

    return max(lidiameter(root.left) + rdiamter(root.right), height(root.left)+ height(root.right) +1

    

if __name__ == '__main__':
    root = create_tree()
    inorder(root)

    print ''
    print 'Height: ', height(root)    
