# 101. Symmetric Tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric
# But the following [1,2,2,null,3,null,3] is not

from BinaryTree import *

class Solution(object):
    def isSymmetric(self, root):
        return self.isMirror(root, root)
        
    def isMirror(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return (root1.val == root2.val) and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)

    def isSymmetric2(self, root):
        if not root:
            return True
        q1 = [root]
        q2 = [root]
        
        while len(q1) > 0:
            root1 = q1.pop(0)
            root2 = q2.pop(0)
            if not root1 and not root2:
                continue
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            q1.append(root1.left)
            q1.append(root1.right)
            q2.append(root2.right)
            q2.append(root2.left)
        return True