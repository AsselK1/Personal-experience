class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def island(grid, i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    island(grid, i + 1, j)
                    island(grid, i - 1, j)
                    island(grid, i, j - 1)
                    island(grid, i, j + 1)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    island(grid, i, j)
        return islands
