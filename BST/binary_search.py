# Binary tree node
class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if not root:
        return

    print(root.data)
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)


def inorder(root):
    if not root:
        return

    if root.left:
        inorder(root.left)
    print(root.data)
    if root.right:
        inorder(root.right)


def postorder(root):
    if not root:
        return

    if root.left:
        postorder(root.left)
    if root.right:
        postorder(root.right)
    print(root.data)


def level(root):
    if root is None:
        return []
    parents = [root]
    new_parents = []
    level = []
    final = []

    while parents:
        for root in parents:
            level.append(root.data)
            if root.left is not None:
                new_parents.append(root.left)
            if root.right is not None:
                new_parents.append(root.right)
        final.append(level)
        level = []
        parents = new_parents
        new_parents = []
    return final


def onlyleaf(root):
    if not root:
        return 0

    if not root.left and not root.right:
        print(root.data)

    if root.left:
        onlyleaf(root.left)

    if root.right:
        onlyleaf(root.right)


def sysmetric(root):
    def isTree(L, R):
        if not L and not R:
            return True
        if L and R and L.data == R.data:
            return isTree(L.left, R.right) and isTree(L.left, R.right)
        return False

    return isTree(root.left, root.right)


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.left.left.left = Node(5)
    root.left.left.right = Node(6)
    root.left.right.left = Node(7)
    root.left.right.right = Node(8)

    root.right = Node(2)
    root.right.right = Node(3)
    root.right.left = Node(4)
    root.right.right.right = Node(5)
    root.right.right.left = Node(6)
    root.right.left.right = Node(7)
    root.right.left.left = Node(8)


    (preorder(root))
    print('In-order')
    (inorder(root))
    print('post-order')
    (postorder(root))
    print(level(root))

    print(onlyleaf(root))
    print(sysmetric(root))
