# 947. Most Stones Removed with Same Row or Column

# On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
# Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
# What is the largest possible number of moves we can make?

# Example 1:
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5

# Example 2:
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3

# Example 3:
# Input: stones = [[0,0]]
# Output: 0
 
# Note:
# 1 <= stones.length <= 1000
# 0 <= stones[i][j] < 10000

from collections import defaultdict

class Solution(object):
    def removeStones(self, stones):
        graph = defaultdict(list)
        for i in range(len(stones)):
            for j in range(i):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)
        visited = set()
        self.count = 0
        def dfs(graph,v):
            visited.add(v)
            for i in graph[v]:
                if i not in visited:
                    self.count += 1
                    dfs(graph,i)
        for i in range(len(stones)):
            if i not in visited:
                dfs(graph,i)
        return self.count

class Solution2(object):
    def removeStones(self, stones):
        parents = [-1] * len(stones)
        
        def find(x):
            if parents[x] < 0:
                return x
            return find(parents[x])
        def union(x, y):
            xRoot = find(x)
            yRoot = find(y)
            if xRoot != yRoot:
                if parents[xRoot] < parents[yRoot]:
                    parents[xRoot] += parents[yRoot]
                    parents[yRoot] = xRoot
                else:
                    parents[yRoot] += parents[xRoot]
                    parents[xRoot] = yRoot
                    
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
                 
        for i in range(len(parents)):
            if parents[i] > 0:
                count += 1

        return count

sol = Solution2()
sol.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
                
        