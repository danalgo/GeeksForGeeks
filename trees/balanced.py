"""
The difference in the height of the left subtree and
the right subtree can be maximum of one
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

def is_bal(root):
    if root is None:
        return True, 0
    l_isbal, lh = is_bal(root.left)
    r_isbal, rh = is_bal(root.right)
    if l_isbal and r_isbal and abs(lh-rh) <= 1:
        return l_isbal, max(lh, rh) + 1
    else:
        return False, max(lh,rh) + 1

if __name__ == '__main__':
    root = create_tree()
    inorder(root)

    print ''
    print 'Is tree balanced: ', is_bal(root)
