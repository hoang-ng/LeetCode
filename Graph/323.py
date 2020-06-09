# 323. Number of Connected Components in an Undirected Graph

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

# Example 1:
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

#      0          3
#      |          |
#      1 --- 2    4 
# Output: 2

# Example 2:
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

#      0           4
#      |           |
#      1 --- 2 --- 3
# Output:  1

# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

import collections

def countComponents(self, n, edges):
        parent = [-1] * n
        def find(x):
            if parent[x] == -1:
                return x
            return find(parent[x])
        def union(x, y):
            xRoot = find(x)
            yRoot = find(y)
            if xRoot != yRoot:
                parent[xRoot] = yRoot
                
        for x, y in edges:
            union(x, y)
            
        count = 0
        for i in range(len(parent)):
            if parent[i] == -1:
                count += 1
        
        return count

class Solution2(object):
    def countComponents(self, n, edges):
        graph = collections.defaultdict(list)
        visited = [False] * n
        
        for src,dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        def dfs(node):
            visited[node] = True
            
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
            return 

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count +=1
        return count

