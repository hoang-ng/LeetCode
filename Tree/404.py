# 404. Sum of Left Leaves

# Find the sum of all left leaves in a given binary tree.

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        ans = 0
        if root.left and not root.left.left and not root.left.right:
            ans += root.left.val
        ans += self.sumOfLeftLeaves(root.left)
        ans += self.sumOfLeftLeaves(root.right)
        
        return ans