# 226. Invert Binary Tree

class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root

class Solution2(object):
    def invertTree(self, root):
        if not root:
            return None
        self.invert(root, root.left, root.right)
        return root
        
    def invert(self, root, left, right):
        if not root:
            return
        
        root.left = right
        root.right = left
        if left:
            self.invert(left, left.left, left.right)
        if right:
            self.invert(right, right.left, right.right)