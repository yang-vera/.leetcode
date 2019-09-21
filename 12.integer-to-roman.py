#
# @lc app=leetcode id=12 lang=python
#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (51.78%)
# Likes:    686
# Dislikes: 2118
# Total Accepted:    264.5K
# Total Submissions: 507.4K
# Testcase Example:  '3'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
# 
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# For example, two is written as II in Roman numeral, just two one's added
# together. Twelve is written as, XII, which is simply X + II. The number
# twenty seven is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
# 
# 
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# 
# 
# Given an integer, convert it to a roman numeral. Input is guaranteed to be
# within the range from 1 to 3999.
# 
# Example 1:
# 
# 
# Input: 3
# Output: "III"
# 
# Example 2:
# 
# 
# Input: 4
# Output: "IV"
# 
# Example 3:
# 
# 
# Input: 9
# Output: "IX"
# 
# Example 4:
# 
# 
# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# 
# 
# Example 5:
# 
# 
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# 
#
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str = []
        num_M = num // 1000
        str.append('M'*num_M)
        num -= 1000 * num_M
        if num >= 900:
            str.append('CM')
            num -= 900
        elif num >= 500:
            str.append('D')
            num -= 500
        elif num >= 400:
            str.append('CD')
            num -= 400
        
        num_C = num // 100
        str.append('C'*num_C)
        num -= 100 * num_C
        
        if num >= 90:
            str.append('XC')
            num -= 90
        elif num >= 50:
            str.append('L')
            num -= 50
        if num >= 40:
            str.append('XL')
            num -=40
        num_X = num // 10
        str.append('X'*num_X)
        num -= 10 * num_X
        
        if num == 9:
            str.append('IX')
            return ''.join(str)
        if num == 4:
            str.append('IV')
            return ''.join(str)
        if num >= 5:
            str.append('V')
            num -= 5
        str.append('I'*num)
        return ''.join(str)
        
        

