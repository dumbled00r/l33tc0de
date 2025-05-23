"""
There is a bi-directional graph with n vertices, where each vertex is labeled from
0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges,
 where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
 Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a
valid path from source to destination, or false otherwise.

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
"""

from collections import defaultdict
from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)


        # build the graph
        graph = defaultdict(list)
        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)

        seen = {source}
        dfs(source)

        return destination in seen
if __name__ == "__main__":
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    solution = Solution()
    print(solution.validPath(6, edges, 0, 5))
