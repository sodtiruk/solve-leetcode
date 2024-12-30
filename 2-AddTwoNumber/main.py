# Definition for singly-linked list.
# class ListNode(object):
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type li1: Optional[ListNode] 
        :type li2: Optional[ListNode] 
        :rtype: Optional[ListNode]
        """

        head = ListNode()
        l3 = head
        carry = 0 
        while l1 != None or l2 != None:
            
            if l1 == None: l1v = 0
            else: l1v = l1.val
            if l2 == None: l2v = 0
            else: l2v = l2.val

            total = l1v + l2v + carry
            carry = total//10
            lastDigit = total%10

            l3.next = ListNode(lastDigit)
            l3 = l3.next

            if l1 != None:
                l1 = l1.next
                l2 = l2.next

        if carry > 0:
            l3.next = ListNode(carry)
            l3 = l3.next
        return head.next


