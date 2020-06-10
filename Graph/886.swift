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

class Solution {
    func possibleBipartition(_ N: Int, _ dislikes: [[Int]]) -> Bool {
        let noColor = 0
        let black = 1
        
        var graph = [[Int]](repeating: [Int](), count: N+1)
        for edge in dislikes {
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        }
        
        var colors = Array(repeating: 0, count: N + 1)
        
        func dfs(_ i: Int, _ color: Int) -> Bool {
            colors[i] = color
            for nei in graph[i] {
                if colors[nei] == color {
                    return false
                }
                if colors[nei] == 0 && !dfs(nei, -color) {
                    return false
                }
            }
            
            return true
        }
        
        for i in 1...N {
            if colors[i] == 0 {
                if !dfs(i, black) {
                    return false
                }
            }
        }
        
        return true
    }
}