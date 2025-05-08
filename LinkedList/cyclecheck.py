"""
Example 2: 141. Linked List Cycle

Given the head of a linked list, determine if the linked list has a cycle.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
"""



def checkCycle(head):
    slow = head
    fast = head

    while fast and fast.next: # fast pointer has not reached the end

        slow = slow.next
        fast = fast.next.next
        # if a node is visited twice (that means, slow == fast), pointing to a same element --> there is a loop/cycle
        if slow == fast:
            return True

    return False