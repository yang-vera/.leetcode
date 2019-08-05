#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (33.85%)
# Likes:    1778
# Dislikes: 91
# Total Accepted:    324.6K
# Total Submissions: 957.6K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1 
            else:
                return [self.target_left(nums, left, right, target), self.target_right(nums, left, right, target)]
        return [-1, -1]

    
    def target_left(self, nums, start, end, target):
        while start <= end:
            mid = (start+end)//2
            if nums[mid] < target:
                start = mid + 1
            else:
                if mid == 0 or target > nums[mid-1]: 
                    return mid
                else: 
                    end = mid - 1
    
    def target_right(self, nums, start, end, target):
        while start <= end:
            mid = (start+end)//2
            if nums[mid] > target:
                end = mid - 1
            else:
                if mid == len(nums)-1 or target < nums[mid+1]: 
                    return mid
                else: 
                    start = mid + 1
    
