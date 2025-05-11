"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: Optional[TreeNode]) -> int:
    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        if left and right:
            return 1 + min(left, right) # has 2 children --> return the smallest height of 2 children

        if not left and not right:
            return 1 # at leaf node --> height of 1

        if left:
            return 1+left
        return 1+right

    return dfs(root)


"""
The following code builds a tree that looks like:
            3
          /   \
         9    20
             /  \
            15   7
"""
"""
The following code builds a tree that looks like:
             2
              \
               3
                \
                 4
                  \
                   5
                    \
                     6
"""


if __name__ == "__main__":
    # node0 = TreeNode(3)
    # node1 = TreeNode(9)
    # node2 = TreeNode(20)
    # node3 = TreeNode(15)
    # node4 = TreeNode(7)
    #
    # node0.left = node1
    # node0.right = node2
    #
    #
    # node2.left = node3
    # node2.right = node4

    node0 = TreeNode(2)
    node1 = TreeNode(3)
    node2 = TreeNode(4)
    node3 = TreeNode(5)
    node4 = TreeNode(6)

    node0.right = node1
    node1.right = node2
    node2.right = node3
    node3.right = node4
    print(minDepth(node0))


