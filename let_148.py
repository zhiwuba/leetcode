# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge_list(a: ListNode, b: ListNode):
            result = ListNode()
            cur = result
            while a!= None and b!= None:
                if a.val > b.val:
                    cur.next = b
                    b = b.next
                else:
                    cur.next = a
                    a = a.next
                cur = cur.next
            while a!= None:
                cur.next = a
                a = a.next
                cur = cur.next

            while b!=None:
                cur.next = b
                b = b.next
                cur = cur.next
            return result.next

        def split_list(a: ListNode):
            if a.next == None:
                return a, None
            quick_ptr = a
            slow_ptr = ListNode(next=a)
            while quick_ptr != None and quick_ptr.next != None:
                slow_ptr = slow_ptr.next
                quick_ptr = quick_ptr.next.next
            list_b = a
            list_c = slow_ptr.next
            slow_ptr.next = None
            return list_b, list_c

        def my_sort(a: ListNode):
            if a == None:
                return a
            if a.next == None:
                return a
            b, c = split_list(a)
            return merge_list(my_sort(b), my_sort(c))
        return my_sort(head)