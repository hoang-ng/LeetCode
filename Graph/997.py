# 997. Find the Town Judge

# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:
# 1. The town judge trusts nobody.
# 2. Everybody (except for the town judge) trusts the town judge.
# 3. There is exactly one person that satisfies properties 1 and 2.

# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1

# Example 1:
# Input: N = 2, trust = [[1,2]]
# Output: 2

# Example 2:
# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3

# Example 3:
# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1

# Example 4:
# Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1

# Example 5:
# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3

class Solution(object):
    def findJudge(self, N, trust):
        incoming = [0] * N
        outgoing = [0] * N
        for i in range(len(trust)):
            outgoing[trust[i][0] - 1] += 1
            incoming[trust[i][1] - 1] += 1
        
        for i in range(N):
            if outgoing[i] == 0 and incoming[i] == N - 1:
                return i + 1
        return -1

    def findJudge2(self, N, trust):
        trustCount = [0] * (N + 1)
        for i, j in trust:
            trustCount[i] -=1
            trustCount[j] += 1
        for i in range(1, N + 1):
            if trustCount[i] == N - 1:
                return i
        return -1