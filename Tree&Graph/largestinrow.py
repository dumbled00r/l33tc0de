"""
Example 2: 515. Find Largest Value in Each Tree Row

Given the root of a binary tree, return an array of the largest value in each row of the tree.
"""



from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largestValues(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    ans = []
    queue = deque([root])

    while queue:
        currMax = float("-inf")
        nodes_in_current_row = len(queue)

        for i in range(nodes_in_current_row):
            node = queue.popleft()

            if node.val >= currMax:
                currMax = node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        ans.append(currMax)



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

    print(largestValues(node0))
