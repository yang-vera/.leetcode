#
# @lc app=leetcode id=1048 lang=python
#
# [1048] Longest String Chain
#
# https://leetcode.com/problems/longest-string-chain/description/
#
# algorithms
# Medium (50.51%)
# Likes:    433
# Dislikes: 30
# Total Accepted:    30.1K
# Total Submissions: 57.3K
# Testcase Example:  '["a","b","ba","bca","bda","bdca"]'
#
# Given a list of words, each word consists of English lowercase letters.
# 
# Let's say word1 is a predecessor of word2 if and only if we can add exactly
# one letter anywhere in word1 to make it equal to word2.  For example, "abc"
# is a predecessor of "abac".
# 
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >=
# 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of
# word_3, and so on.
# 
# Return the longest possible length of a word chain with words chosen from the
# given list of words.
# 
# 
# 
# Example 1:
# 
# 
# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
    
    """


        # Write your code here
        # sort the words array from shortest to longest
        words.sort(key=lambda s:len(s))
        length = len(words) # length of the words array
        maxLenChain = 0
        # dynamic programming
        # dp[i] is the longest string chain from index 0 to i 
        dp = [1]*length 
        for i in range(length):
            iLen = len(words[i])
            for j in range(i):
                # j < i, len(words[j]) <= len(words[i])
                if len(words[j]) + 1 < iLen:
                    # words[i] cannot be reduced to words[j]
                    continue
                elif len(words[j]) ==iLen:
                    # words[j] [j+1]...[i-1] has the same length as words[i]
                    # words[i] cannot be reduced to them
                    break
                else:
                    if checkReduce(words[j], words[i], iLen-1):
                        dp[i] = max(dp[i], dp[j]+1)
                        maxLenChain = max(maxLenChain , dp[i])
        return maxLenChain 

        

def checkReduce(word1, word2, dim_word1):
    ignore = 0
    for i in range(dim_word1):
        if word1[i]==word2[i+ignore]:
            continue
        elif ignore == 0:
            ignore=1
        else:
            return False
    return True

# @lc code=end

