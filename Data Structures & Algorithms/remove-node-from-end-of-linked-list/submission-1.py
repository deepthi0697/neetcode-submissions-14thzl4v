# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        fast = dummy
        slow = dummy
        for _ in range(n+1):
            if fast is None: 
                return None
            fast = fast.next
        # print(fast.val)
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next= slow.next.next

        return dummy.next
