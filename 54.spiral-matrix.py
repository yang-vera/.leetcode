#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (30.97%)
# Likes:    1234
# Dislikes: 433
# Total Accepted:    251.3K
# Total Submissions: 811.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return
        result = []
        self.one_loop(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1, result)
        return result

    def one_loop(self, matrix, r_l, r_h, c_l, c_h, result):
        if r_l > r_h or c_l > c_h:
            return
        #------>
        for i in range(c_l, c_h+1):
            result.append(matrix[r_l][i])
        #----- down
        for i in range(r_l+1, r_h+1):
            result.append(matrix[i][c_h])
        #----- left
        if r_l < r_h:
            for i in range(c_h-1, c_l-1, -1):
                result.append(matrix[r_h][i])
        #----- up
        if c_l < c_h:        
            for i in range(r_h-1, r_l,-1):
                result.append(matrix[i][c_l])
        self.one_loop(matrix, r_l+1, r_h-1,c_l+1,c_h-1, result)  

        

