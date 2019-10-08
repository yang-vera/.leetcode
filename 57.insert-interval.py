#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
class Solution:
    def insert(self, intervals, newInterval):
        res = []
        for i in range(len(intervals)):
            one_list = intervals[i]
            if one_list[1]<newInterval[0]:
                res.append(one_list)
            else:
                if one_list[0]>newInterval[1]:
                    res.append(newInterval)
                    return res + intervals[i:]
                else:
                    newInterval[0] = min(newInterval[0], one_list[0])
                    newInterval[1] = max(newInterval[1], one_list[1])
        return res + [newInterval]

#print(Solution().insert([[1,3],[6,9]],[2,5] ))
