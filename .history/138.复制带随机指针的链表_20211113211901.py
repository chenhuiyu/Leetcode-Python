'''
Date: 2021-11-13 21:09:24
LastEditors: Chenhuiyu
LastEditTime: 2021-11-13 21:19:00
FilePath: \\.leetcode\\138.复制带随机指针的链表.py
'''
#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        hashmap={}
        cur =head
        while cur is not None:
# @lc code=end

