"""
Example 4: 100. Same Tree

Given the roots of two binary trees p and q, check if they are the same tree.
Two binary trees are the same tree if they are structurally identical and the nodes have the same values.
"""


"""
Example 2: 112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if there exists a path from the root to a leaf
such that the sum of the nodes on the path is equal to targetSum, and return false otherwise.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    left = isSameTree(p.left, q.left)
    right = isSameTree(p.right, q.right)

    return left and right


def iterativeSolution(p: TreeNode, q: TreeNode) -> bool:
    stack = [(p, q)]

    while stack:
        p, q = stack.pop()

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        stack.append((p.left, q.left))
        stack.append((p.right, q.right))

    return True


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
    print(isSameTree(node0, node0))


