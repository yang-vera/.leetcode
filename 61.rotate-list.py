#
# @lc app=leetcode id=61 lang=python
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (28.04%)
# Likes:    733
# Dislikes: 886
# Total Accepted:    216.3K
# Total Submissions: 770.5K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, rotate the list to the right by k places, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# 
# 
# Example 2:
# 
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #检验是否有东西
        if not head or k == 0:
            return head
        onenode = tail = head
        i = 0
        while onenode:
            i+=1
            if not onenode.next:
                tail = onenode
            onenode=onenode.next
        # tail node is found length of the list is known
        # find which node to be rotated
        nodeL = i
        #余数 找一个例子比较即可
        index = k % nodeL
        if index == 0:
            return head
        onenode = head
        for i in range(0,nodeL-index-1): 
            onenode=onenode.next

        tail.next = head
        head = onenode.next 
        onenode.next = None
        return head

# @lc code=end

