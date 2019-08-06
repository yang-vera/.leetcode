#
# @lc app=leetcode id=31 lang=python
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (30.74%)
# Likes:    1955
# Dislikes: 621
# Total Accepted:    253.3K
# Total Submissions: 823K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i-=1
        if i == 0:
            nums.reverse()
            return
        j, k = i-1, len(nums)-1
        while nums[k]<=nums[j]:
            k-=1
        nums[j], nums[k] = nums[k], nums[j]
        nums[j+1:]=nums[:j:-1]

