# 226. Invert Binary Tree

# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

# Output:
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1(object):
    def invertTree(self, root):
        if not root:
            return None

        queue = [root]

        while queue:
            curr = queue.pop(0)
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return root


class Solution2(object):
    def invertTree(self, root):
        if root:
            left = root.left
            right = root.right

            root.left = self.invertTree(right)
            root.right = self.invertTree(left)
        return root
