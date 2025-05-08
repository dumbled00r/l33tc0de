"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
from collections import defaultdict
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head


        while ptr1:
            while ptr1.next and ptr1.next.val == ptr1.val:
                ptr1.next = ptr1.next.next

            ptr1 = ptr1.next

        return head


def main():
    node1= ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)

    node1.next = node2
    node2.next = node3

    a = Solution()
    ans = a.deleteDuplicates(node1)
    while ans:
        print(f"{ans.val}-->", end="")
        ans = ans.next

if __name__ == "__main__":
    main()