#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (33.02%)
# Likes:    2666
# Dislikes: 336
# Total Accepted:    446.9K
# Total Submissions: 1.4M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left <=right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if (nums[left] <= target < nums[mid]) or \
                ((nums[mid] < nums[left]) and (target >= nums[left] or target < nums[mid])):
                right = mid - 1
                continue
            if (nums[mid]< target <= nums[right]) or \
                ((nums[mid] > nums[right]) and (target > nums[mid] or target <= nums[right])):
                left = mid + 1
                continue
            return -1
        




        

