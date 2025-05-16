"""
Example 2: 863. All Nodes Distance K in Binary Tree

Given the root of a binary tree, a target node target in the tree, a
nd an integer k, return an array of the values of all nodes that have a distance k from the target node.
"""

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # first, we will have to build up a undirected graph
        def dfs(node, parent):
            if not node:
                return

            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)


        dfs(root, None)

        # use BFS now

        queue = deque([target])
        seen = {target}
        dist = 0

        while queue and dist < k: ## dist == k ?
            number_of_nodes_in_the_level = len(queue)
            for i in range(number_of_nodes_in_the_level):

                node = queue.popleft()
                for neighbor in [node.left, node.right, node.parent]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            dist += 1
        return [node.val for node in queue]

# """
# The following code builds a tree that looks like:
#             0
#           /   \
#          1     2
#        /   \    \
#       3     4    5
#              \
#               6
# """
if __name__ == "__main__":
    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node0.left = node1
    node0.right = node2

    node1.left = node3
    node1.right = node4

    node2.right = node5

    node4.right = node6

    solution = Solution()
    print(solution.distanceK(node0, node2, 2))
