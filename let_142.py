# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        quick_ptr = head
        slow_ptr = head
        ptr = head

        while(quick_ptr!= None and slow_ptr!= None and quick_ptr.next!= None):
            quick_ptr = quick_ptr.next.next
            slow_ptr = slow_ptr.next

            if quick_ptr == slow_ptr:
                while True:
                    if ptr == slow_ptr:
                        return ptr
                    ptr = ptr.next
                    slow_ptr = slow_ptr.next

        return None