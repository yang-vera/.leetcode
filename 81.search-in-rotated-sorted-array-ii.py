#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        left, right = 0, len(nums)-1
        while left <=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return True
            elif nums[left]<=target<nums[mid] or \
                (nums[mid]<=nums[left] and (target<nums[mid] or nums[left]<=target)):
                right = mid-1
            elif nums[mid]<=target<nums[right] or \
                (nums[mid]>=nums[right] and (target>nums[mid] or target<=nums[right] )):
                left = mid+1
            else:
                return False
        

