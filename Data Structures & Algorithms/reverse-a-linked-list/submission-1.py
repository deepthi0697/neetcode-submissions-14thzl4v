# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev, curr = None, head
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev
        dummy = ListNode()
        curr = head
        while curr:
            nxt = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = nxt
        return dummy.next         

