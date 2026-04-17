class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        curr = head
        total_len = 0
        while curr:
            total_len += 1
            curr = curr.next
        mid = (total_len + 1) // 2

        list1 = head
        for i in range(1, mid):
            list1 = list1.next
        
        list2_start = list1.next
        list1.next = None 

        prsnt = list2_start
        rev = ListNode()

        while prsnt:
            nxt = prsnt.next
            prsnt.next = rev.next
            rev.next = prsnt
            prsnt = nxt

        l1 = head.next
        l2 = rev.next
        curr = head

        for i in range(1, total_len):
            if i % 2 != 0:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next