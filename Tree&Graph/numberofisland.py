"""
Example 2: 200. Number of Islands

Given an m x n 2D binary grid which represents a map of 1 (land) and 0 (water),
 return the number of islands. An island is surrounded by water and is formed by connecting adjacent land cells horizontally or vertically.
"""



from collections import defaultdict
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '1':
                return
            else:
                grid[row][col] = '0'
                dfs(row, col+1) ## to the right
                dfs(row+1, col) ## bottom
                dfs(row, col-1) ## left
                dfs(row-1, col) ## top

        num_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)

        return num_islands

    ### second way
    def numIslandsV2(self, grid: List[List[str]]) -> int:

        def isLand(row, col):
            return 0 <= row < rows and 0 <= col < cols and grid[row][col] == '1'

        def dfs(row, col):
            for dx, dy in directions:
                next_row, next_col = row+dx, col+dy
                if isLand(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    # perform one dfs on the next row/col pair
                    dfs(next_row, next_col)

        directions = [(1, 0), # go to bottom
                      (-1, 0), # go to top
                      (0, 1), # go to right
                      (0, -1)] # go to left
        rows, cols = len(grid), len(grid[0])

        seen = set()
        ans = 0

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and grid[row][col] == '1':
                    ans+=1
                    seen.add((row, col))
                    dfs(row, col)

        return ans





if __name__ == "__main__":
    grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
    solution = Solution()
    print(solution.numIslands(grid))