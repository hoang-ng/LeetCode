
# 437. Path Sum III

# You are given a binary tree in which each node contains an integer value.
# Find the number of paths that sum to a given value.
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Example:
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# Return 3. The paths that sum to 8 are:
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


from BinaryTree import (generateBinaryTree, TreeNode)

class Solution(object):
    def pathSum(self, root, sum):
        def dfs(root, preSum, sum):
            if not root:
                return 0
            currSum = preSum + root.val
            count = 0
            if (currSum - sum) in dic:
                count += dic[currSum - sum]
            if currSum in dic:
                dic[currSum] += 1
            else:
                dic[currSum] = 1
            count += dfs(root.left, currSum, sum)
            count += dfs(root.right, currSum, sum)
            dic[currSum] -= 1
            return count
        dic = {0: 1}
        return dfs(root, 0, sum)

root = generateBinaryTree([5,4,8,11,-1,13,4,7,2,-1,-1,5,1])
sol = Solution()
sol.pathSum(root, 22)
        