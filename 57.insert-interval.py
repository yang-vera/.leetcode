#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        length = len(intervals)
        new_l = newInterval[0]
        new_r = newInterval[1]
        left=[]
        right=[]
        for num_list in intervals:
            if num_list[0]> new_r:
                right.append(num_list)
            elif num_list[1] < new_l:
                left.append(num_list)
            else:
                new_l=min(new_l, num_list[0])
                new_r=max(new_r, num_list[1])
        return left + [[new_l, new_r]] + right

