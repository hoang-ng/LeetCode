# 872. Leaf-Similar Trees

# Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

from BinaryTree import *

def leafSimilar(self, root1, root2):
    def dfs(root, leaves):
        if not root:
            return
        if not root.left and not root.right:
            leaves.append(root.val)
        dfs(root.left, leaves)
        dfs(root.right, leaves)

    leaves1 = []
    dfs(root1, leaves1)
    leaves2 = []
    dfs(root2, leaves2)

    if len(leaves1) == len(leaves2):
        for i in range(len(leaves1)):
            if leaves1[i] != leaves2[i]:
                return False
        return True
    else:
        return False
