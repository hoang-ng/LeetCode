# 783. Minimum Distance Between BST Nodes

# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

class Solution(object):
    def minDiffInBST(self, root):
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if not self.lastNode:
                self.lastNode = root
            else:
                self.ans = min(root.val - self.lastNode.val, self.ans)
                self.lastNode = root
            dfs(root.right)
            
        self.lastNode = None
        self.ans = float("inf")
        dfs(root)
        return self.ans