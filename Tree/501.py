# 501. Find Mode in Binary Search Tree

# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

class Solution(object):
    def findMode(self, root):
        if not root:
            return None
        def dfs(root, count):
            if not root:
                return
            count[root.val] = count.get(root.val, 0) + 1
            dfs(root.left, count)
            dfs(root.right, count)
        count = {}
        dfs(root, count)
        maxi = max(count.values())
        ans = []
        for i in count:
            if maxi == count[i]:
                ans.append(i)
        return ans