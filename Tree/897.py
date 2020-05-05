# 897. Increasing Order Search Tree

# Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

# Example 1:
# Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

from BinaryTree import TreeNode

class Solution(object):
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.curr.right = node
                self.curr = node
                inorder(node.right)
        ans = self.curr = TreeNode(None)
        inorder(root)
        return ans.right

    def increasingBST2(self, root):
        vals = self.inorder(root)
        
        ans = curr = TreeNode(0)
        for val in vals:
            curr.right = TreeNode(val)
            curr = curr.right
        return ans.right
        
    def inorder(self, root):
        if not root:
            return []
        rs = []
        rs += self.inorder(root.left)
        rs += [root.val]
        rs += self.inorder(root.right)
        return rs