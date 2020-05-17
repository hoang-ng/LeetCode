from BinaryTree import *

class Solution(object):
    @staticmethod
    def maxLevelSum(root): #BFS
        queue = [root]
        ans = 0
        
        currLv = 0
        maxLvSum = -float("inf")
        
        while len(queue) > 0:
            size = len(queue)
            currSum = 0
            currLv += 1
            for _ in range(size):
                node = queue.pop(0)
                currSum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if currSum > maxLvSum:
                maxLvSum = currSum
                ans = currLv
        return ans
    
    @staticmethod
    def maxLevelSum2(self, root): #DFS
        sumLv = {}
        def dfs(root, lv, sumLv):
            if not root:
                return
            currSum = sumLv.get(lv, 0)
            sumLv[lv] = currSum + root.val
            dfs(root.left, lv + 1, sumLv)
            dfs(root.right, lv + 1, sumLv)
        dfs(root, 1, sumLv)
        
        maxSum = -float("inf")
        ans = 0
        for k in sumLv.keys():
            if sumLv[k] > maxSum:
                maxSum = sumLv[k]
                ans = k
        return ans 