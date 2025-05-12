"""
Example 1: 199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it.
 Return the values of the nodes you can see ordered from top to bottom.
"""


from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    ans = []
    queue = deque([root])

    while queue:
        nodes_in_current_level = len(queue)
        ans.append(queue[-1].val)

        for i in range(nodes_in_current_level):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

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

    print(rightSideView(node0))
