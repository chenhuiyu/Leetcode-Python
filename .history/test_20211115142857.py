'''
Date: 2021-11-15 02:50:54
LastEditors: Chenhuiyu
LastEditTime: 2021-11-15 14:28:22
FilePath: \\.leetcode\\test.py
'''
nums = [3, 2, 1, 6, 0, 5]
low = 0
high = 5
max = max(nums[low:high])
max_index = nums[high:low].index(max)
