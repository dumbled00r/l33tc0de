from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root: # the node is not valid
        return 0

    leftMax = maxDepth(root.left)
    rightMax = maxDepth(root.right)

    return 1+max(leftMax, rightMax)

# iterative solution
def iterativeMaxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    stack = [(root, 1)] # store node and current depth of the node
    ans = 0

    while stack:
        # use preorder
        node, depth = stack.pop()
        ans = max(ans, depth)

        if node.left:
            stack.append((node.left, depth + 1))

        if node.right:
            stack.append((node.right, depth + 1))

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

    print(maxDepth(node0))
    print(iterativeMaxDepth((node0)))


