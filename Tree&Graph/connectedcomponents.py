"""
You have a graph of n nodes. You are given an integer n and an array
edges where edges[i] = [ai, bi] indicates that there is an edge between
ai and bi in the graph.

Return the number of connected components in the graph.


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

"""

from collections import defaultdict
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build the graph first seen edges list was given
        graph = defaultdict(list)
        for start, dest in edges:
            graph[start].append(dest)
            graph[dest].append(start)

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        seen = set()
        ans = 0
        ### this does not consider nodes that do not connect with others
        # for _ in graph:
        #     for neighb in graph[_]: ### armotized O(1) ?
        #         if neighb not in seen:
        #             ans += 1
        #             seen.add(neighb)
        #             dfs(neighb)

        for _ in range(n):
            if _ not in seen:
                ans += 1
                seen.add(_)
                dfs(_)
        return ans

if __name__ == "__main__":
    edges = [[2,3],[1,2],[1,3]]
    solution = Solution()
    print(solution.countComponents(4, edges))
