# 102. Binary Tree Level Order Traversal

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        queue = [root]
        ans = []
        while len(queue) > 0:
            size = len(queue)
            arr = []
            for _ in range(size):
                node = queue.pop(0)
                arr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(arr)
        return ans