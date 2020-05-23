# 144. Binary Tree Preorder Traversal

# Given a binary tree, return the preorder traversal of its nodes' values.

# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?

class Solution1(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        ans = []
        
        while len(stack) > 0:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans

class Solution2(object):
    def preorderTraversal(self, root):
        def dfs(root):
            if not root:
                return
            rs.append(root.val)
            dfs(root.left)
            dfs(root.right)
        rs = []
        dfs(root)
        return rs