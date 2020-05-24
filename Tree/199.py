# 199. Binary Tree Right Side View

# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example:

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

class Solution1(object):
    def rightSideView(self, root):
        dic = {}
        rs = []
        self.dfs(root, 0, dic, rs)
        return rs
        
    def dfs(self, root, lv, dic, rs):
        if not root:
            return
        if lv not in dic:
            rs.append(root.val)
        dic[lv] = 1
        self.dfs(root.right, lv + 1, dic, rs)
        self.dfs(root.left, lv + 1, dic, rs)

class Solution2(object):
    def rightSideView(self, root):
        rs = []
        if not root:
            return rs
        queue = [root]
        
        while len(queue) > 0:
            size = len(queue)
            flag = False
            for i in range(size):
                if not flag:
                    rs.append(queue[len(queue) - 1].val)
                    flag = True
                node = queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return rs