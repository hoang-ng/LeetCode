# 637. Average of Levels in Binary Tree

# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

from BinaryTree import TreeNode

class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return []
        queue = [root]
        rs = []
        
        while len(queue) > 0:
            size = len(queue)
            s = 0.0
            for _ in range(size):
                node = queue.pop(0)
                s += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rs.append(s / size)
        
        return rs

    def averageOfLevels2(self, root):
        info = []
        def dfs(node, depth = 0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)
        
        return [s/float(c) for s, c in info]