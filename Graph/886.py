# 886. Possible Bipartition

# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
# Each person may dislike some other people, and they should not go into the same group. 
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
# Return true if and only if it is possible to split everyone into two groups in this way.

# Example 1:
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]

# Example 2:
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false

# Example 3:
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false

# Constraints:
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# dislikes[i].length == 2
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].

import collections

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        NOT_COLOR, BLUE, GREEN = 0, 1, -1
        
        def dfs(i, color):
            colors[i] = color
            for nei in graph[i]:
                if colors[nei] == color:
                    return False
                if colors[nei] == NOT_COLOR and not dfs(nei, -color):
                    return False
            return True
        
        if N == 1 and len(dislikes) == 0:
            return True
        
        graph = collections.defaultdict(list)
        colors = [NOT_COLOR] * (N + 1)
        
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            
        for i in range(1, N + 1):
            if colors[i] == NOT_COLOR:
                if not dfs(i, BLUE):
                    return False
        
        return True

sol = Solution()
sol.possibleBipartition(4, [[1,2],[1,3],[2,4]])