# 965. Univalued Binary Tree

# A binary tree is univalued if every node in the tree has the same value.
# Return true if and only if the given tree is univalued.

# Example 1:
# Input: [1,1,1,1,1,null,1]
# Output: true

# Example 2:
# Input: [2,2,2,5,2]
# Output: false

# Note:
# 1. The number of nodes in the given tree will be in the range [1, 100].
# 2. Each node's value will be an integer in the range [0, 99].

class Solution(object):
    def isUnivalTree(self, root):
        vals = []
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return len(set(vals)) == 1

    def isUnivalTree2(self, root):
        if not root:
            return True
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)