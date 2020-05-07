# 100. Same Tree

# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

from BinaryTree import TreeNode

class Solution(object):
    def isSameTree(self, p, q):
        def preOrder(node):
            if not node:
                return [-1]
            rs = []
            rs.append(node.val)
            rs += preOrder(node.left)
            rs += preOrder(node.right)
            return rs
        
        nodes1 = preOrder(p)
        nodes2 = preOrder(q)
        
        return nodes1 == nodes2
    
    def isSameTree2(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)