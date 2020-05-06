# 257. Binary Tree Paths

# Given a binary tree, return all root-to-leaf paths.
# Note: A leaf is a node with no children.

# Example:
# Input: [1, 2, 3, null, 5]
# Output: ["1->2->5", "1->3"]
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

class Solution(object):
    def binaryTreePaths(self, root):
        def dfs(root, paths, rs):
            if not root:
                return
            if not root.left and not root.right:
                rs.append(paths + str(root.val))
        
            dfs(root.left, paths + str(root.val) + "->", rs)
            dfs(root.right, paths + str(root.val) + "->", rs)
        rs = []
        dfs(root, "", rs)
        return rs