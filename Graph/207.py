# 207. Course Schedule

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
 
# Constraints:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10^5

import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        
        for u, v in prerequisites:
            graph[v].append(u)
            
        def isCyclic(u, checked, path):
            if checked[u]:
                return False
            if path[u]:
                return True
            
            path[u] = True

            ret = False
            for child in graph[u]:
                ret = isCyclic(child, checked, path)
                if ret: break
            path[u] = False
            checked[u] = True
            return ret
                    
        checked = [False] * numCourses
        path = [False] * numCourses
        
        for i in range(numCourses):
            if isCyclic(i, checked, path):
                return False
                
        return True
        
class Solution2:
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(set)
        for i, j in prerequisites:
            graph[i].add(j)

        visited = [0] * numCourses
        self.foundCycle = False
        
        def dfs(start):
            if self.foundCycle:   
                return
            if visited[start] == 1:
                self.foundCycle = True
            if visited[start] == 0:
                visited[start] = 1 
            for i in graph[start]:
                dfs(i)
            visited[start] = 2
        
        for i in range(numCourses):
            if self.foundCycle: 
                break
            if visited[i] == 0:
                dfs(i)

        return not self.foundCycle

     
sol = Solution2()
sol.canFinish(2, [[1,0],[0,1]])