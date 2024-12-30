# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(-1)
        list3 = head

        while list1 != None or list2 != None:

            if list1 == None and list2 != None:
                list3.next = ListNode(list2.val)
                list3 = list3.next
            elif list2 == None and list1 != None:
                list3.next = ListNode(list1.val)
                list3 = list3.next
            else:
                if list1.val >= list2.val:
                    list3.next = ListNode(list2.val)
                    list3 = list3.next                

                    list3.next = ListNode(list1.val)
                    list3 = list3.next

                elif list1.val < list2.val:
                    list3.next = ListNode(list1.val)
                    list3 = list3.next                

                    list3.next = ListNode(list2.val)
                    list3 = list3.next
            if list1 != None:
                list1 = list1.next
            if list2 != None:
                list2 = list2.next
        return head.next


head1 = ListNode(-1)
list1 = head1

list1.next = ListNode(1)
list1 = list1.next
list1.next = ListNode(2)
list1 = list1.next
list1.next = ListNode(4)
list1 = list1.next


head2 = ListNode(-1)
list2 = head2

list2.next = ListNode(1)
list2 = list2.next
list2.next = ListNode(2)
list2 = list2.next
list2.next = ListNode(4)
list2 = list2.next

s = Solution()
