class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        total_negative = 0
        for i in range(m):
            for j in range(n-1, -1, -1):
                if grid[i][j] >= 0:
                    break

                total_negative += 1

        return total_negative
