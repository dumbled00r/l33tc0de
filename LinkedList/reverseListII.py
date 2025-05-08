"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input: head = [5], left = 1, right = 1
Output: [5]
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummynode = ListNode(0, head)
        curr = head
        leftprev = None
        for _ in range(left-1):
            leftprev = curr
            curr = curr.next

        prev = None
        for i in range(right - left + 1):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        leftprev.next.next = curr
        leftprev.next = prev

        return dummynode.next


        # prev = None
        # i = right-left
        # while i > 0:
        #     nextNode = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nextNode
        #     i -= 1
        # return curr



def main():

    node1= ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    a = Solution()
    left = 2
    right = 4
    ans = a.reverseBetween(node1, left, right)
    while ans:
        print(f"{ans.val}-->", end="")
        ans = ans.next

if __name__ == "__main__":
    main()