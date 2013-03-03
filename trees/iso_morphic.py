
"""
If the two trees can be formed by swapping the 
left and the right child. Then it is a iso-morphic
trees
"""

def is_isomorphic(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None:
        return False
    elif root2 is None:
        return False
    else:
        if root1.data == root2.data:
            if (is_isomorphic(root1.left, root2.left) and is_isomorphic(root1.left, root2.right)) or ( is_isomorphic(root1.right, root2.left) and is_isomorphic(root1.right, root2.right)):
            return True
    return False

if __name__ == '__main__':
    is_isomorphic(root1, root2)
