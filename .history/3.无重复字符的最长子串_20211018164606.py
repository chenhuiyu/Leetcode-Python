'''
Date: 2021-10-18 16:07:17
LastEditors: Chenhuiyu
LastEditTime: 2021-10-18 16:46:06
FilePath: \\leetcode_pythonc:\\Users\\Administrator\\.leetcode\\3.无重复字符的最长子串.py
'''

#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}

        for index, char in enumerate(s):
            if char not in hashmap:
                hashmap[char] = index
            last_repeat_index = -1


# @lc code=end
