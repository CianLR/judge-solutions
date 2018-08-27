# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lt_head = lt = ListNode(None)
        ge_head = ge = ListNode(None)
        while head:
            if head.val < x:
                lt.next = head
                lt = lt.next
            else:
                ge.next = head
                ge = ge.next
            head = head.next
        ge.next = None
        lt.next = ge_head.next
        return lt_head.next
        
