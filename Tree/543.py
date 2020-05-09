# 543. Diameter of Binary Tre

# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# from BinaryTree import (generateBinaryTree, TreeNode)

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.best = 0
        def dfs(root):
            if not root:
                return 0
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            self.best = max(self.best, leftHeight + rightHeight)

            return max(leftHeight, rightHeight) + 1

        dfs(root)
        return self.best