'''
Date: 2021-11-15 21:57:07
LastEditors: Chenhuiyu
LastEditTime: 2021-11-15 22:00:26
FilePath: \\.leetcode\\652.寻找重复的子树.py
'''

#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # 将所有子树序列化
        def help(root):
            if root is None:
                return "#"
            # 序列化左子树
            left = help(root.left)
            # 序列化右子树
            right = help(root.right)
            # 序列化当前子树
            serial_subtree = left + "," + str(root.val) + "," + right
            # 查询当前子树是否出现在hashmap中
            if serial_subtree not in hashmap:
                hashmap[serial_subtree] = 1
            else:
                hashmap[serial_subtree] += 1
                if hashmap[serial_subtree] == 2:
                    ans.append(root)

        hashmap = {}


# @lc code=end
