# 547. Friend Circles

# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.
# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

# Example 1:
# Input: 
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
# The 2nd student himself is in a friend circle. So return 2.

# Example 2:
# Input: 
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

# Note:
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.

class Solution(object):
    def findCircleNum(self, M):
        visited = [False] * len(M)
        count = 0
        for i in range(len(M)):
            if not visited[i]:
                self.dfs(M, i, visited)
                count += 1
        return count
    
    def dfs(self, M, u, visited):
        if not visited[u]:
            visited[u] = True
            for v in range(len(M[u])):
                if M[u][v] == 1 and not visited[v]:
                    self.dfs(M, v, visited)

class Solution2(object):
    def find(self, parent, i):
        if parent[i] == -1:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, x, y):
        xset = self.find(parent, x)
        yset = self.find(parent, y)
        if xset != yset:
            parent[xset] = yset
    
    def findCircleNum(self, M):
        parent = [-1] * len(M)
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1 and i != j:
                    self.union(parent, i, j)
        
        count = 0
        for i in range(len(parent)):
            if parent[i] == -1:
                count += 1
        return count


sol = Solution()
sol.findCircleNum([[1,1,0,1], [1,1,0,0], [0,0,1,0], [1,0,0,1]])