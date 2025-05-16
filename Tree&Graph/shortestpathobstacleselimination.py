"""
Example 4: 1293. Shortest Path in a Grid with Obstacles Elimination

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). Y
ou can move up, down, left, or right from and to an empty cell in one step.
Return the minimum number of steps to walk from the upper left corner to the lower right corner given that you can
eliminate at most k obstacles. If it is not possible, return -1.

Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
"""


from typing import List
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def isValid(row,col):
            return 0 <= row < m and 0 <= col < n
        m = len(grid)
        n = len(grid[0])
        queue = deque([(0, 0, k, 0)])
        seen = {(0, 0, k)}


        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        # now bfs
        while queue:
            row, col, remain, steps = queue.popleft()
            if row == m - 1 and col == n - 1:
                return steps

            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if isValid(next_row, next_col):
                    if grid[next_row][next_col] == 0:
                        if (next_row, next_col, remain) not in seen:
                            seen.add((next_row, next_col, remain))
                            queue.append((next_row, next_col, remain, steps + 1))
                    elif remain and (next_row, next_col, remain-1) not in seen:
                        seen.add((next_row, next_col, remain-1))
                        queue.append((next_row, next_col, remain-1, steps + 1))

        return -1

if __name__ == "__main__":
    mat = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
    solution = Solution()
    print(solution.shortestPath(mat,1))