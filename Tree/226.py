# 226. Invert Binary Tree

class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root