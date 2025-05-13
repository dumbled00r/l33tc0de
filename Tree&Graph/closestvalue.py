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
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        values = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
        dfs(root)
        currMin = float("+inf")
        ans = []
        for i, val in enumerate(values):
            if abs(target - val) < currMin:
                currMin = abs(target - val)
                ans.append((currMin, i))
        return values[ans[-1][1]]

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

    solution = Solution()
    print(solution.closestValue(None, 4.428571))