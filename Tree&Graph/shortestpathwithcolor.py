"""
Example 5: 1129. Shortest Path with Alternating Colors

You are given a directed graph with n nodes labeled from 0 to n - 1.
Edges are red or blue in this graph.
 You are given redEdges and blueEdges,
  where redEdges[i] and blueEdges[i] both have the format [x, y] indicating an edge from x to y in the respective color.
Return an array ans of length n, where answer[i] is the length of the shortest path from 0 to i
where edge colors alternate, or -1 if no path exists.

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]

"""




from typing import List
from collections import deque, defaultdict


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        RED = 0
        BLUE = 1
        # build the graph
        graph = defaultdict(lambda : defaultdict(list))
        for x, y in redEdges:
            graph[RED][x].append(y)
        for x, y in blueEdges:
            graph[BLUE][x].append(y)
        print(graph)

        ans = [float("inf")]*n
        q = deque([(0, RED, 0), (0, BLUE, 0)]) # node, color, steps

        seen = {(0, RED), (0, BLUE)}

        while q:
            node, color, steps = q.popleft()
            ans[node] = min(ans[node], steps)

            for neighbor in graph[color][node]:
                if (neighbor, 1 - color) not in seen:
                    seen.add((neighbor, 1-color))
                    q.append((neighbor, 1-color, steps + 1))

        return [x if x != float("inf") else -1 for x in ans]

if __name__ == "__main__":
    n = 3
    redEdges = [[0,1]]
    blueEdges = [[2,1]]
    solution = Solution()
    print(solution.shortestAlternatingPaths(n,redEdges, blueEdges))