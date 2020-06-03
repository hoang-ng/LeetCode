# 785. Is Graph Bipartite?

# Given an undirected graph, return true if and only if it is bipartite.
# Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.
# The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

# Example 1:
# Input: [[1,3], [0,2], [1,3], [0,2]]
# Output: true
# Explanation: 
# The graph looks like this:
# 0----1
# |    |
# |    |
# 3----2
# We can divide the vertices into two groups: {0, 2} and {1, 3}.

# Example 2:
# Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
# Output: false
# Explanation: 
# The graph looks like this:
# 0----1
# | \  |
# |  \ |
# 3----2
# We cannot find a way to divide the set of nodes into two independent subsets.
 
# Note:
# graph will have length in range [1, 100].
# graph[i] will contain integers in range [0, graph.length - 1].
# graph[i] will not contain i or duplicate values.
# The graph is undirected: if any element j is in graph[i], then i will be in graph[j].

class Solution(object):
    def isBipartite(self, graph):
        n = len(graph)
        if len(graph) <= 1:
            return True
        
        NON_COLOR, BLACK, WHITE = 0, 1, -1
        colors = [NON_COLOR] * n
        
        def dfs(i, color):
            colors[i] = color
            
            for j in graph[i]:
                if colors[j] == color:
                    return False
                if colors[j] == NON_COLOR:
                    if not dfs(j, -color):
                        return False
            return True
        
        for i in range(len(graph)):
            if colors[i] == NON_COLOR:
                if not dfs(i, BLACK):
                    return False
                
        return True
        