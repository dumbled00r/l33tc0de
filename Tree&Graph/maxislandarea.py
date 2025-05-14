"""
You are given an m x n binary matrix grid. An island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""


from collections import defaultdict
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            size = 0
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1:
                return size
            else:
                grid[row][col] = 0
                size += 1
                size += dfs(row-1, col)
                size += dfs(row+1, col)
                size += dfs(row, col-1)
                size += dfs(row, col+1)

            return size


        maxSize = float("-inf")
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    sz = dfs(i,j)
                    if sz > maxSize:
                        maxSize = sz

        return maxSize if maxSize > float("-inf") else 0




if __name__ == "__main__":
    grid =  [[0,0,0,0,0,0,0,0]]
    solution = Solution()
    print(solution.maxAreaOfIsland(grid))