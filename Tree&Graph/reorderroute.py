"""
Example 3: 1466. Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities.
Roads are represented by connections where connections[i] = [x, y] represents a road from city x to city y. The edges are directed.
You need to swap the direction of some edges so that every city can reach city 0. Return the minimum number of swaps needed.


Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
"""


from collections import defaultdict
from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        roads = set()
        # build undirected graph
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x,y))


        def dfs(node):
            ans = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node, neighbor) in roads:
                        ans+=1
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans

        seen = {0}
        return dfs(0)

if __name__ == "__main__":
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    solution = Solution()
    print(solution.minReorder(6, connections))