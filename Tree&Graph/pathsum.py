"""
Example 2: 112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if there exists a path from the root to a leaf
such that the sum of the nodes on the path is equal to targetSum, and return false otherwise.
"""

from typing import Optional

from sympy import false


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root: Optional[TreeNode], k) -> int:
    def dfs(node, curr):
        if not node:
            return false

        if not node.left and not node.right:
            return (node.val + curr) == k
        curr += node.val
        left = dfs(node.left, curr)
        right = dfs(node.right, curr)

        return left or right

    return dfs(root, 0)


# iterative solution

def iterativePathSum(root: Optional[TreeNode], k) -> int:
    if not root:
        return False


    stack = [(root, 0)]
    while stack:
        node, curr = stack.pop()
        if not node.left and not node.right: # at leaf
            if curr + node.val == k:
                return True

        curr += node.val

        if node.left:
            stack.append((node.left, curr))
        if node.right:
            stack.append((node.right, curr))

    return False




"""
The following code builds a tree that looks like:
            0
          /   \
         1     2
       /   \    \
      3     4    5
             \
              6
"""
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

    targetSum = 11
    print(pathSum(node0, 11))


