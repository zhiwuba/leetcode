# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addon = 0
        result = None
        cur = None
        while l1 != None and l2 != None:
            val = l1.val + l2.val + addon
            if val >= 10:
                addon = 1
                val = val - 10
            else:
                addon = 0

            if result is None:
                result = ListNode(val=val)
                cur = result
            else:
                cur.next = ListNode(val=val)
                cur = cur.next

            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            val = l1.val + addon
            if val >= 10:
                addon = 1
                val = val - 10
            else:
                addon = 0
            cur.next = ListNode(val=val)
            cur = cur.next
            l1 = l1.next

        while l2 != None:
            val = l2.val + addon
            if val >= 10:
                addon = 1
                val = val - 10
            else:
                addon = 0
            cur.next = ListNode(val=val)
            cur = cur.next
            l2 = l2.next

        if addon >= 1:
            cur.next = ListNode(val=addon)
            cur = cur.next

        return result