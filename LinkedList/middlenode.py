"""
Example 1: Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.

For example, given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3.
"""


def getmiddle(head):
    slow = head
    fast = head
    while fast and fast.next: ## this is to ensure fast has not reached the end of the list
        slow = slow.next
        fast = fast.next.next

    # return current slow val --> when fast reached the end --> that is the middle node
    return slow.val