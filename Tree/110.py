# 110. Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:
# Given the following tree [3,9,20,null,null,15,7]:
# Return true.

# Example 2:
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# Return false.

class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        return abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def getHeight(self, root):
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def isBalanced2(self, root):
        return self.dfsHeight (root) != -1;
    
    def dfsHeight(self, root):
        if not root:
            return 0
        leftHeight = self.dfsHeight(root.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.dfsHeight(root.right)
        if rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        return 1 + max(self.dfsHeight(root.left), self.dfsHeight(root.right))