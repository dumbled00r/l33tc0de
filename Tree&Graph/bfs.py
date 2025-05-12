"""
implementatiopn of breadth first search
"""

from collections import deque

def traverse(root):
    queue = deque([root])

    while queue:
        nodes_in_current_level = len(queue)

        # do some logic here for current level

        for i in range(nodes_in_current_level):
            node = queue.popleft()

            # do some logic here for current node

            print(node.val)

            # put next level into queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)