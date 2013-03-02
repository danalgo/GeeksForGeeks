
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

def common_ancestor(first, second, root, ancestors):
    if root is None:
        return
    if root.data is first.data:
        # Found first node
        print ancestors
    if root.data is second.data:
        # Found second node
        print ancestors
    common_ancestor(first, second, root.left, ancestors + [root.data])


if __name__=='__main__':
    root = create_tree() 
    
    print 'Common Ancestors between', root.left.data, 'and', root.left.right.data 
    common_ancestor(root.left, root.left.right, root, [])
