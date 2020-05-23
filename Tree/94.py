# 94. Binary Tree Inorder Traversal

# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

from BinaryTree import generateBinaryTree, TreeNode

class Solution(object):
    def inorderTraversal(self, root):
        rs = []
        self.dfs(root, rs)
        return rs
        
    def dfs(self, root, rs):
        if not root:
            return
        self.dfs(root.left, rs)
        rs.append(root.val)
        self.dfs(root.right, rs)

class Solution2(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        rs = []
        stack = []
        curr = root
        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            rs.append(curr.val)
            curr = curr.right
        return rs