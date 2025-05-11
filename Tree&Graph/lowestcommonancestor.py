"""
Bonus example: 236. Lowest Common Ancestor of a Binary Tree

Given the root of a binary tree and two nodes p and q that are in the tree,
return the lowest common ancestor (LCA) of the two nodes. The LCA is the lowest node in the tree
that has both p and q as descendants (note: a node is a descendant of itself).
"""



from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return None # since root == None --> there is no LCA (no descendant at all)


    # in case p or q is the root node
    if root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root

    if left:
        return left

    return right




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
    print(lowestCommonAncestor(node0, node2, node3))