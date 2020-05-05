# 617. Merge Two Binary Trees

# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

class Solution(object):
    def mergeTrees(self, t1, t2):
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
    
    def mergeTrees2(self, t1, t2):
        if not t1:
            return t2
        
        stack = [[t1, t2]]
        while len(stack) > 0:
            t = stack.pop()
            if not t[0] or not t[1]:
                continue
            t[0].val += t[1].val
            if not t[0].left:
                t[0].left = t[1].left
            else:
                stack.append([t[0].left, t[1].left])
            if not t[0].right:
                t[0].right = t[1].right
            else:
                stack.append([t[0].right, t[1].right])
        return t1