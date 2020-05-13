# 687. Longest Univalue Path

# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
# The length of path between two nodes is represented by the number of edges between them.

class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0
        def dfs(root):
            if not root:
                return 0
            left_length = dfs(root.left)
            right_length = dfs(root.right)
            
            left_arrow = right_arrow = 0
            if root.left and root.left.val == root.val:
                left_arrow = left_length + 1
            if root.right and root.right.val == root.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)
        dfs(root)
        return self.ans