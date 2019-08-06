#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (28.41%)
# Likes:    1314
# Dislikes: 75
# Total Accepted:    181.7K
# Total Submissions: 638.1K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# Example:
# 
# 
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# Note:
# 
# You can assume that you can always reach the last index.
# 
#
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        nstep = 1
        step_min = 1
        step_max = 0 + nums[0]
        while step_min<=step_max:
            if step_max >= len(nums)-1:
                return nstep
            else:
                nstep+=1
                last_max = step_max
                for i in range(step_min, step_max+1):
                    step_max = max(i + nums[i], step_max)
                step_min = last_max + 1


        

