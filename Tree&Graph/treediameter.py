"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

# max left + max right?


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeDiameter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            self.diameter = max(self.diameter, leftMax + rightMax)

            return max(leftMax, rightMax) + 1

        dfs(root)
        return self.diameter






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
    print(solution.treeDiameter(node0))
