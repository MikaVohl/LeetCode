from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_node = None
        if not head:
            return None
        next_node = head.next
        while next_node:
            head.next = last_node
            last_node = head
            head = next_node
            next_node = next_node.next
        head.next = last_node
        return head