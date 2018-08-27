# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        end = head
        for i in xrange(k):
            if end.next is None:
                return self.rotateRight(head, k % (i + 1))
            end = end.next
        
        k_back = head
        while end.next:
            end = end.next
            k_back = k_back.next
        
        end.next = head
        new_start = k_back.next
        k_back.next = None
        return new_start
        
