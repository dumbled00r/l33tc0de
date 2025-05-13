"""
Example 3: 98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid BST.
"""


from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def dfs(node, lower, upper):
        if not node:
            return True

        if not (lower < node.val < upper):
            return False

        left = dfs(node.left, lower, node.val)
        right = dfs(node.right, node.val, upper)

        return left and right

    lower = float('-inf')
    upper = float('inf')
    return dfs(root, lower, upper)





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


    print(isValidBST(node0))
