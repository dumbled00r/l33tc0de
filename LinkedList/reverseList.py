from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    ### iterative
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     curr = head
    #     prev = None
    #
    #     while curr:
    #         nextNode = curr.next
    #         curr.next = prev # reverse the arrow
    #         prev = curr
    #         curr = nextNode
    #
    #     return prev

    # recursive solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None # empty linked list

        if not head.next:
            return head # reached the end of the list

        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return prev


def main():

    node1= ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    a = Solution()
    ans = a.reverseList(node1)
    while ans:
        print(f"{ans.val}-->", end="")
        ans = ans.next

if __name__ == "__main__":
    main()