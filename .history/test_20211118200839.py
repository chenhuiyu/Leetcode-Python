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

        def processing(board, i, j, row, col, bucket):
            print(i, j)
            # 如果来到最后一个，返回true
            if i == 8 and j == 8:
                return True
            if j == 8:
                next_j = 0
                next_i = i + 1
            else:
                next_i = i
                next_j = j + 1
            # 不需要填
            if board[i][j] != '.':
                # 直接跳下一个
                return processing(board, next_i, next_j, row, col, bucket)
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
                        if processing(board, next_i, next_j, row, col, bucket) is True:
                            print(i, j, n, processing(board, next_i, next_j, row, col, bucket))
                            return True
                        # 回复递归现场
                        row[i][num - 1] = 0
                        col[j][num - 1] = 0
                        bucket[k][num - 1] = 0
                        board[i][j] = "."
                # return False

        processing(board, 0, 0, row, col, bucket)