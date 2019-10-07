#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
        '''
        if m==1 or n==1:
            return 1
        dp = [1]*m
        for i in range(1,n):
            for j in range(1,m):
                dp[j]=dp[j]+dp[j-1]
        return dp[-1]

