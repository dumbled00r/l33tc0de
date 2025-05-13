"""
Example 1: 938. Range Sum of BST

Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range [low, high].

"""


from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    if not root:
        return 0

    ans = 0
    if low <= root.val <= high:
        ans += root.val

    if root.val > low:
        ans += rangeSumBST(root.left, low, high)
    if root.val < high:
        ans += rangeSumBST(root.right, low, high)

    return ans

def iterativeRangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    stack = [root]
    ans = 0

    while stack:
        node = stack.pop()

        if low <= node.val <= high:
            ans += node.val

        if node.left and node.val > low:
            stack.append(node.left)
        if node.right and node.val < high:
            stack.append(node.right)
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


    print(iterativeRangeSumBST(node0, 7, 15))
