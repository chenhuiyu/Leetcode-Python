'''
Date: 2021-10-18 17:16:14
LastEditors: Chenhuiyu
LastEditTime: 2021-10-18 20:04:08
FilePath: \\leetcode_pythonc:\\Users\\Administrator\\.leetcode\\4.寻找两个正序数组的中位数.py
'''
#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
# @lc code=end


def f(n):
    return 2**(len(bin(n & -n))-2)-1
