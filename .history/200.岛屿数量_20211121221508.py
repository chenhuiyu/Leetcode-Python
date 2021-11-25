#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#


# @lc code=start
class Solution:
    def infection(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "2"
        infection(grid, i + 1, j)
        infection(grid, i - 1, j)
        infection(grid, i, j + 1)
        infection(grid, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    self.infection(grid, i, j)


# @lc code=end
