# 113. Path Sum II

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# Note: A leaf is a node with no children.

# Example:
# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

class Solution(object):
    def pathSum(self, root, sum):
        rs = []
        self.dfs(root, sum, [], rs)
        return rs
        
    def dfs(self, root, sum, tmpList, rs):
        if root:
            if not root.left and not root.right:
                if sum == root.val:
                    rs.append(tmpList + [root.val])
            self.dfs(root.left, sum - root.val, tmpList + [root.val], rs)
            self.dfs(root.right, sum - root.val, tmpList + [root.val], rs)