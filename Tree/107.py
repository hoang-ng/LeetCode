# 107. Binary Tree Level Order Traversal II

# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

from BinaryTree import *

class Solution(object):
    def levelOrderBottom(self, root):
        res = []
        self.levelMaker(root, 0, res)
        return res
        
    def levelMaker(self, root, level, res):
        if not root:
            return
        if len(res) < level + 1:
            res.insert(0, [])
        res[len(res) - level - 1].append(root.val)
        self.levelMaker(root.left, level + 1, res)
        self.levelMaker(root.right, level + 1, res)
    
    def levelOrderBottom1(self, root):
        if not root:
            return None
        rs = []
        queue = [root]
        while len(queue) > 0:
            size = len(queue)
            nodes = []
            for _ in range(size):
                node = queue.pop(0)
                nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rs.insert(0, nodes)

        return rs


root = generateBinaryTree([3, 9, 20, -1, -1, 15, 7])
sol = Solution()
sol.levelOrderBottom(root)