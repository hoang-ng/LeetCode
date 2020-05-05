# 104. Maximum Depth of Binary Tree

# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.

# Example:
# Given binary tree [3,9,20,null,null,15,7]
# return its depth = 3

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        queue = [root]
        dept = 0
        while len(queue) > 0:
            dept += 1
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return dept

    def maxDepth2(self, root):
        if not root:
            return 0
        dept = 0
        dept = max(dept, self.maxDepth(root.left))
        dept = max(dept, self.maxDepth(root.right))
        return dept + 1