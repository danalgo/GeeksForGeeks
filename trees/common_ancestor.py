
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

def least_common_ancestor(root, p, q):
    if root is None:
        return None
    if root.left is p or root.right is q or root.right is p or root.left is q:
        # Root is the common ancestor
        return root
    else:
        # Check it in left subtree
        l = least_common_ancestor(root.left, p, q)
        r = least_common_ancestor(root.right, p, q)
        
        if l is None and r is None:
            return None 
        elif l is None and r is not None:
            return root 
        elif l is not None and r i None:
            return root


if __name__=='__main__':
    root = create_tree() 
    
    print 'Common Ancestors between', root.left.data, 'and', root.left.right.data 
    common_ancestor(root.left, root.left.right, root, [])
