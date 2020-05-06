class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateBinaryTree(arr, i = 0):
    if i >= len(arr):
        return None
    val = arr[i]
    if val == -1:
        return None
    node = TreeNode(val)
    node.left = generateBinaryTree(arr, 2 * i + 1)
    node.right = generateBinaryTree(arr, 2 * i + 2)
    return node