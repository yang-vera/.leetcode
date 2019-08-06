#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.77%)
# Likes:    1100
# Dislikes: 82
# Total Accepted:    348.4K
# Total Submissions: 761.2K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result_min = nums[0] + nums[1] + nums[2]
        diff_min = abs(result_min-target)
        length = len(nums)
        for i in range(length-2):
            j, k= i+1, length-1
            while j < k:
                result = nums[i]+nums[j]+nums[k]
                diff = abs(result - target)
                if result == target:
                    return result
                else:
                    if abs(diff) < diff_min:
                        result_min = result
                        diff_min = diff
                    if result < target:
                        j+=1
                    else:
                        k-=1
            
        return result_min



        

