# 111. Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Given binary tree [3,9,20,null,null,15,7],
# return its minimum depth = 2.

from BinaryTree import *

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        return min(left, right) + 1

    def minDepth2(self, root):
        if not root:
            return 0
        q = [root]
        i = 0
        while len(q) > 0:
            i += 1
            k = len(q)
            for _ in range(k):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if not node.left and not node.right:
                    return i
        return -1

root = generateBinaryTree([3,9,20,-1,-1,15,7])
sol = Solution()
print(sol.minDepth2(root))