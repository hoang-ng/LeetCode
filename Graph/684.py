# 684. Redundant Connection

# In this problem, a tree is an undirected graph that is connected and has no cycles.
# The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.
# Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
#   1
#  / \
# 2 - 3

# Example 2:
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
#     |   |
#     4 - 3
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

import collections

class Solution(object):
    def findRedundantConnection(self, edges):
        parent = [-1] * len(edges)
        
        def find(x):
            if parent[x] == -1:
                return x
            return find(parent[x])
        
        def union(x, y):
            xRoot = find(x)
            yRoot = find(y)
            if xRoot != yRoot:
                parent[xRoot] = yRoot
                return True
            return False
        
        for x, y in edges:
            if not union(x - 1, y - 1):
                return [x, y]
        return []

class Solution2(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)
        
        def dfs(s, d):
            if s not in seen:
                seen.add(s)
                if s == d:
                    return True
                for n in graph[s]:
                    if dfs(n, d):
                        return True
            return False
        
        for u,v in edges:
            seen = set()
            if dfs(u,v):
                return [u,v]
                
            graph[u].add(v)
            graph[v].add(u)

sol = Solution2()
sol.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])