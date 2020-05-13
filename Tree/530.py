# 530. Minimum Absolute Difference in BST

# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

class Solution(object):
    def getMinimumDifference(self, root):
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