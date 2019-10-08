#
# @lc app=leetcode id=32 lang=python
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (26.06%)
# Likes:    2278
# Dislikes: 104
# Total Accepted:    216.8K
# Total Submissions: 822.4K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#
#zy: dynamic programming
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0]*len(s)
        for i in range(1, len(s)):
            if s[i]=='(':
                continue
            else:
                if s[i-1]=='(':
                    if i-2>=0:
                        dp[i]=dp[i-2]+2
                    else:
                        dp[i]=2
                else:
                    start = i -dp[i-1]-1
                    if start < 0:
                        continue
                    if s[start] == ')':
                        continue
                    else:
                        if start -1 >=0:
                            dp[i]=dp[i-1]+dp[start-1]+2
                        else:
                            dp[i]=dp[i-1]+2
        return max(dp)

        
        


