#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#


# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def infection(borad, i, j):
            if board[i][j] == "O":
                board[i][j] = "."
                infection(borad, i + 1, j)
                infection(borad, i, j + 1)
                infection(borad, i - 1, j)
                infection(borad, i, j - 1)


# @lc code=end
