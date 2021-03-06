#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = nums[0]
        for i in range(len(nums)):
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + nums[i])
            if max_jump >= len(nums) - 1:
                return True


# @lc code=end
