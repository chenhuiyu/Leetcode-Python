#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#


# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col, bucket = self.cal_bool(board)
        self.processing(board, 0, 0, row, col, bucket)

    def processing(self, board, i, j, row, col, bucket):
        # 如果来到最后一个，返回true
        if j == 9:
            j = 0
            i += 1
            if i == 9:
                return True
        # 不需要填
        if board[i][j] != '.':
            # 直接跳下一个
            return self.processing(board, i, j + 1, row, col, bucket)
            # return processing(board, next_i, next_j, row, col, bucket)
        # 需要填
        else:
            k = 3 * (i // 3) + j // 3
            # 遍历填入数字1-9
            for n in range(1, 10, 1):
                # 通过限制数组剪枝
                if row[i][n - 1] == 0 and col[j][n - 1] == 0 and bucket[k][n - 1] == 0:
                    # board[i][j]填入n，修改限制数组
                    row[i][n - 1] = 1
                    col[j][n - 1] = 1
                    bucket[k][n - 1] = 1
                    # 递归跳下一个
                    board[i][j] = str(n)
                    # print(processing(board, next_i, next_j, row, col, bucket))
                    if self.processing(board, i, j + 1, row, col, bucket) is True:
                        return True
                    # 回复递归现场
                    row[i][n - 1] = 0
                    col[j][n - 1] = 0
                    bucket[k][n - 1] = 0
                    board[i][j] = "."
        return False

    def cal_bool(self, board):
        row = [[0 for i in range(9)] for j in range(9)]
        col = [[0 for i in range(9)] for j in range(9)]
        bucket = [[0 for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                k = 3 * (i // 3) + j // 3
                if board[i][j] != ".":
                    num = int(board[i][j])
                    row[i][num - 1] = 1
                    col[j][num - 1] = 1
                    bucket[k][num - 1] = 1
        return row, col, bucket


# @lc code=end
