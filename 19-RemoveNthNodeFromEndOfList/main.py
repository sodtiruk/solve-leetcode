# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        first = head
        second = head
        count = 0
        while second != None:
            second = second.next
            if count > n:
                first = first.next

            count += 1
        
        if count == n:
            return head.next

        first.next = first.next.next 
        return head 



