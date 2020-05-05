# 559. Maximum Depth of N-ary Tree

# Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

# Example 1:
# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3

# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: 5

# Constraints:
# The depth of the n-ary tree is less than or equal to 1000.
# The total number of nodes is between [0, 10^4].

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        dept = 0
        queue = [root]
        
        while len(queue) > 0:
            dept += 1
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                for child in node.children:
                    queue.append(child)
        return dept

    def maxDepth2(self, root):
        if not root:
            return 0
        dept = 0
        for child in root.children:
            dept = max(dept, self.maxDepth(child))
        return 1 + dept