"""
Example 5: 1557. Minimum Number of Vertices to Reach All Nodes

Given a directed acyclic graph, with n vertices numbered from 0 to n-1, a
nd an array edges where edges[i] = [x, y] represents a directed edge from node x to node y.
Find the smallest set of vertices from which all nodes in the graph are reachable.

Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex.
 From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].

Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node,
so we must include them. Also any of these vertices can reach nodes 1 and 4.
"""

from collections import defaultdict
from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        degree = [0]*n
        for start,end in edges:
            degree[end] += 1

        ans = []
        for i in range(len(degree)):
            if degree[i] == 0:
                ans.append(i)
        return ans



if __name__ == "__main__":
    edges  = [[0,1],[0,2],[2,5],[3,4],[4,2]]
    solution = Solution()
    print(solution.findSmallestSetOfVertices(6, edges ))