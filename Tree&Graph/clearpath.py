"""
Example 1: 1091. Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
If there is no clear path, return -1. A clear path is a path from the top-left cell (0, 0) to the bottom-right cell (n - 1, n - 1)
such that all visited cells are 0. You may move 8-directionally (up, down, left, right, or diagonally).

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

Input: grid = [[0,1],[1,0]]
Output: 2
"""




from collections import defaultdict, deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        def isValid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0

        n = len(grid)
        seen = {(0,0)}
        queue = deque([(0, 0, 1)]) # row, col, # steps
        directions = [
            (0, 1),
            (1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
            (0, -1),
            (-1, 0)
        ]
        while queue:
            row, col, steps = queue.popleft()
            if (row, col) == (n-1, n-1):
                return steps

            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if isValid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps+1))
        return -1



if __name__ == "__main__":
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    solution = Solution()
    print(solution.shortestPathBinaryMatrix(grid))