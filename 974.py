class Solution(object):
    def subarraysDivByK(self, A, K):
        currSum = 0
        preSumDict = {0: 1}
        res = 0
        for n in A:
            currSum += n
            currRem = currSum % K
            if currRem in preSumDict:
                res += preSumDict[currRem]
            preSumDict[currRem] = preSumDict.get(currRem, 0) + 1


sol = Solution()
sol.subarraysDivByK([4,5,0,-2,-3,1], 5)