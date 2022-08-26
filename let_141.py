# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        quick_ptr = head
        slow_ptr = head

        while quick_ptr != None and quick_ptr.next != None and slow_ptr != None:

            quick_ptr = quick_ptr.next.next

            slow_ptr = slow_ptr.next

            if quick_ptr == slow_ptr:
                return True
        return False