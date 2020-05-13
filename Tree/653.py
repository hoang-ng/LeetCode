# 653. Two Sum IV - Input is a BST

# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

class Solution(object):
    def findTarget(self, root, k):
        def dfs(root):
            if not root:
                return []
            arr = []
            arr += dfs(root.left)
            arr += [root.val]
            arr += dfs(root.right)
            return arr
        arr = dfs(root)
        l = 0
        r = len(arr) - 1
        while l < r:
            s = arr[l] + arr[r]
            if s == k:
                return True
            if s > k:
                r -= 1
            else:
                l += 1
        return False