#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (47.96%)
# Likes:    1522
# Dislikes: 42
# Total Accepted:    248.6K
# Total Submissions: 518.4K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n_r = len(grid)
        n_l = len(grid[0])
        if n_r == 1 or n_l==1:
            nstep = sum([sum(num_ar) for num_ar in zip(*grid)])
            return nstep
        for i in range(1, n_r):
            grid[i][0]+=grid[i-1][0]
        for i in range(1, n_l):
            grid[0][i]+=grid[0][i-1]
        for i in range(1,n_l):
            for j in range(1, n_r):
                grid[j][i]+=min(grid[j][i-1], grid[j-1][i])
        return grid[n_r-1][n_l-1]


