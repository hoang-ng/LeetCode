# 990. Satisfiability of Equality Equations

# Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.
# Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

# Example 1:
# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.

# Example 2:
# Input: ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

# Example 3:
# Input: ["a==b","b==c","a==c"]
# Output: true

# Example 4:
# Input: ["a==b","b!=c","c==a"]
# Output: false

# Example 5:
# Input: ["c==c","b==d","x!=z"]
# Output: true
 
# Note:

# 1. 1 <= equations.length <= 500
# 2. equations[i].length == 4
# 3. equations[i][0] and equations[i][3] are lowercase letters
# 4. equations[i][1] is either '=' or '!'
# 5. equations[i][2] is '='

class Solution(object):
    def equationsPossible(self, equations):
        parent = [-1] * 26
            
        def find(x):
            if parent[x] == -1:
                return x
            return find(parent[x])
        
        def union(x, y):
            xRoot = find(x)
            yRoot = find(y)
            if xRoot != yRoot:
                parent[xRoot] = yRoot
        
        check = []
        for a, e, _, b in equations:
            if e == "=":
                union(ord(a) - 97, ord(b) - 97)
            else:
                check.append((a, b))
                
        for a, b in check:
            if find(ord(a) - 97) == find(ord(b) - 97):
                return False
        return True

from collections import defaultdict

class Solution2(object):
    def equationsPossible(self, equations):
        def dfs(u, visited, target):
            if u == target: 
                return True
            visited.add(u)
            for v in neighbors[u]:
                if v in visited: 
                    continue
                if dfs(v, visited, target):
                    return True
            return False
        
        check = []
        neighbors = defaultdict(set)
        for a, e, _, b in equations:
            if e == '!':
                check.append((a, b))
                continue
            neighbors[a].add(b)
            neighbors[b].add(a)
        
        for u, v in check:
            if dfs(u, set(), v):
                return False
        return True

sol = Solution2()
sol.equationsPossible(["a==b","b!=c","c==a"])