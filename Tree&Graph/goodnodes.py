"""
Example 3: 1448. Count Good Nodes in Binary Tree

Given the root of a binary tree, find the number of nodes that are good. A node is good if the path between the root
and the node has no nodes with a greater value.
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countGoodNodes(root: Optional[TreeNode]) -> int:
    def dfs(node, maxSoFar: int) -> int:
        if not node:
            return 0
        numLeftGoodNodes = dfs(node.left, max(maxSoFar, node.val))
        numRightGoodNodes = dfs(node.right, max(maxSoFar, node.val))

        ans = numRightGoodNodes + numLeftGoodNodes

        if node.val >= maxSoFar:
            ans += 1

        return ans

    return dfs(root, float("-inf"))

def iterativeGoodNodes(root: Optional[TreeNode]) -> int:

    if not root:
        return 0

    stack = [(root, float("-inf"))]

    ans = 0

    while stack:
        node, maxSoFar = stack.pop()

        if node.val >= maxSoFar:
            ans += 1

        if node.left:
            stack.append((node.left, max(maxSoFar, node.val)))
        if node.right:
            stack.append((node.right, max(maxSoFar, node.val)))

    return ans

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

    print(countGoodNodes(node0))


