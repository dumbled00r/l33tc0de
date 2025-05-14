"""
There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi]
indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

Note that node 0 will not be a restricted node.

"""


from collections import defaultdict
from typing import List

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        graphneighbor = defaultdict(list)
        for start, dest in edges:
            graphneighbor[start].append(dest)
            graphneighbor[dest].append(start)

        print(graphneighbor)
        seen = set(restricted)
        print(seen)
        def dfs(node):
            cnt = 0
            for neighbor in graphneighbor[node]:
                if neighbor not in seen:
                    cnt += 1
                    seen.add(neighbor)
                    cnt += dfs(neighbor)
            return cnt
        ans = 1
        seen.add(0)
        ans += dfs(0)

        return ans




if __name__ == "__main__":
    edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
    restricted = [4,5]
    solution = Solution()
    print(solution.reachableNodes(7, edges, restricted))