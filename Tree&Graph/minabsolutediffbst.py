"""
Example 2: 530. Minimum Absolute Difference in BST

Given the root of a BST, return the minimum absolute
 difference between the values of any two different nodes in the tree.
"""


from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMinimumDifference(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    def dfs(node) -> None:
        if not node:
            return
        dfs(node.left)
        values.append(node.val)
        dfs(node.right)

    values = []
    dfs(root)
    ans = float("inf")
    for i in range(1, len(values)):
        ans = min(ans, values[i] - values[i - 1])

    return ans

"""
The following code builds a tree that looks like:
            10
          /   \
         5     15
       /   \    \
      3     7    18

"""
if __name__ == "__main__":
    node0 = TreeNode(10)
    node1 = TreeNode(5)
    node2 = TreeNode(15)
    node3 = TreeNode(3)
    node4 = TreeNode(7)
    node5 = TreeNode(18)

    node0.left = node1
    node0.right = node2

    node1.left = node3
    node1.right = node4

    node2.right = node5


    print(getMinimumDifference(node0))
