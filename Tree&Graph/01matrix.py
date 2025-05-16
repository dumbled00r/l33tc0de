"""
Example 3: 542. 01 Matrix

Given an m x n binary (every element is 0 or 1) matrix mat,
find the distance of the nearest 0 for each cell. The distance between adjacent cells (horizontally or vertically) is 1.

For example, given mat = [[0,0,0],[0,1,0],[1,1,1]], return [[0,0,0],[0,1,0],[1,2,1]].

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def isValid(row,col):
            return 0 <= row < m and 0 <= col < n and mat[row][col] == 1
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        seen = set()
        # add all 0 to queue ( since we need to bfs from 0)
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col, 1)) # 1 here is the starting step (every node that are not 0 --> will have 1)
                    seen.add((row, col))

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        # now bfs
        while queue:
            row, col, steps = queue.popleft()

            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if isValid(next_row, next_col) and (next_row, next_col) not in seen:
                    queue.append((next_row, next_col, steps + 1))
                    seen.add((next_row, next_col))
                    mat[next_row][next_col] = steps
        return mat

if __name__ == "__main__":
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    solution = Solution()
    print(solution.updateMatrix(mat))