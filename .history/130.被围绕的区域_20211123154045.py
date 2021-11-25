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
        def infection(board, i, j, bool_ans):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                bool_ans = False
                return
            if board[i][j] == "O":
                board[i][j] = "."
                infection(board, i + 1, j, bool_ans)
                infection(board, i, j + 1, bool_ans)
                infection(board, i - 1, j, bool_ans)
                infection(board, i, j - 1, bool_ans)
                board[i][j] = ""

        # bool_ans = [[1 for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                infection(board, i, j, bool_ans)


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

# @lc code=end
