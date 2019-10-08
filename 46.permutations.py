#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (57.65%)
# Likes:    2469
# Dislikes: 79
# Total Accepted:    441.8K
# Total Submissions: 766.3K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.generateRes(nums, res, [])
        return res
    
    def generateRes(self, nums, res, rec_res):
        if len(rec_res) == len(nums):
            res.append(list(rec_res))
            return
        for i in range(len(nums)):
            if nums[i] in rec_res:
                continue
            else:
                rec_res.append(nums[i])
                self.generateRes(nums, res, rec_res)
                rec_res.pop()

        
# @lc code=end

