# 1282. Group the People Given the Group Size They Belong To

# There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.
# You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution. 

# Example 1:
# Input: groupSizes = [3,3,3,3,3,1,3]
# Output: [[5],[0,1,2],[3,4,6]]
# Explanation: 
# Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

# Example 2:
# Input: groupSizes = [2,1,3,3,3,2]
# Output: [[1],[0,5],[2,3,4]]

# Constraints:
# groupSizes.length == n
# 1 <= n <= 500
# 1 <= groupSizes[i] <= n

import collections

class Solution(object):
    def groupThePeople(self, groupSizes):
        dic = collections.defaultdict(list)
        
        for i in range(len(groupSizes)):
            dic[groupSizes[i]].append(i)
        rs = []
        
        for key in dic.keys():
            count = 0
            subArr = []
            for i in range(len(dic[key])):
                subArr.append(dic[key][i])
                count += 1
                if count == key:
                    rs.append(subArr)
                    subArr = []
                    count = 0
        return rs
        