"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree.
Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
You can return any of them.

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
"""

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)


        return root

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
    print(solution.insertIntoBST(node0, 16))
