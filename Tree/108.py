# 108. Convert Sorted Array to Binary Search Tree

# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:
# Given the sorted array: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5]

from BinaryTree import TreeNode

class Solution(object):
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        return self.constructBST(nums, 0, len(nums) - 1)
    
    def constructBST(self, nums, l, r):
        if l > r:
            return None
        mid = (l + r) / 2
        node = TreeNode(nums[mid])
        node.left = self.constructBST(nums, l, mid - 1)
        node.right = self.constructBST(nums, mid + 1, r)
        return node