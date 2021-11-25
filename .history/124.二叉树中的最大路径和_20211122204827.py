#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def loopInfo(root):
            # 返回两个值，以root为头的最大路径和，包含root的最大路径和
            if root is None: return 0, 0
            if root.left is not None:
                maxPathSumFromHeadLeft, maxPathSumLeft = loopInfo(root.left)
            else:
                maxPathSumFromHeadLeft, maxPathSumLeft = 0, float("-inf")
            if root.right is not None:
                maxPathSumFromHeadRight, maxPathSumRight = loopInfo(root.right)
            else:
                maxPathSumFromHeadRight, maxPathSumRight = 0, float("-inf")

            maxPathSumFromHead = max(root.val, maxPathSumFromHeadLeft + root.val, maxPathSumFromHeadRight + root.val)

            maxPathSum = max(
                maxPathSumLeft,
                maxPathSumRight,
                root.val,
                maxPathSumFromHead,
                maxPathSumFromHeadLeft + root.val + maxPathSumFromHeadRight,
            )
            return maxPathSumFromHead, maxPathSum

        return loopInfo(root)[1]


# @lc code=end

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left=<right:
            while s[left].isalpha() is False:
                left+=1
            while s[right].isalpha() is False:
                right-=1
            if s[left].lower()==s[right].lower():
                left+=1
                right+=1
            else:
                return False
        return True
