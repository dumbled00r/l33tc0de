"""
Example 1: 547. Number of Provinces

There are n cities. A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = isConnected[j][i] = 1 if the
ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise. Return the total number of provinces.
"""

from collections import defaultdict
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        # build the graph
        n = len(isConnected)
        graph = defaultdict(list)


        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        seen = set()
        ans = 0

        for i in range(n):
            if i not in seen:
                # add connected components to a set
                seen.add(i)
                ans += 1
                dfs(i)

        return ans

if __name__ == "__main__":
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    solution = Solution()
    print(solution.findCircleNum(isConnected))