"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
"""
from collections import defaultdict


def equalPairs(grid) -> int:
    counts = defaultdict(int)
    for row in grid:
        counts[tuple(row)] += 1
    ans = 0
    for i in range(len(grid)):
        col = []
        for _ in range(len(grid[i])):
            col.append(grid[_][i])
        if tuple(col) in counts:
            ans+=counts[tuple(col)]
    return ans





print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))





