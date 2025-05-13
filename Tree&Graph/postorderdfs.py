"""
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
If there are multiple answers, print the smallest.

Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Input: root = [1], target = 4.428571
Output: 1
"""
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#
class Solution:
    def quiz(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            print(node.val)

        return dfs(root)





"""
The following code builds a tree that looks like:
            3
          /   \
         7     2
       /   \    \
      6     1    9

"""
if __name__ == "__main__":
    node0 = TreeNode(3)
    node1 = TreeNode(7)
    node2 = TreeNode(2)
    node3 = TreeNode(6)
    node4 = TreeNode(1)
    node5 = TreeNode(9)

    node0.left = node1
    node0.right = node2

    node1.left = node3
    node1.right = node4

    node2.right = node5

    solution = Solution()
    print(solution.quiz(node0))