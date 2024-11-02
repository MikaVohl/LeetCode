from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(val=0, next=None)
        out_curr = output
        while l1 or l2:
            if not l1:
                l1 = ListNode(val=0, next=None)
            if not l2:
                l2 = ListNode(val=0, next=None)
            if l1.next or l2.next or (out_curr.val + l1.val + l2.val >= 10):
                out_curr.next = ListNode(val=((out_curr.val + l1.val + l2.val) // 10), next=None)
            out_curr.val = (out_curr.val + l1.val + l2.val) % 10
            out_curr = out_curr.next
            l1 = l1.next
            l2 = l2.next
        return output