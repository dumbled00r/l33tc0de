"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where
v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.result = 0
        def dfs(node, currMax, currMin):
            if not node:
                return

            if node.val >= currMax:
                currMax = node.val

            if node.val <= currMin:
                currMin = node.val

            self.result = max(self.result, abs(currMax - currMin))
            dfs(node.left, currMax, currMin)
            dfs(node.right, currMax, currMin)


        dfs(root, float("-inf"), float("+inf"))
        return self.result





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
    print(solution.maxAncestorDiff(node0))
