# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        _, new_head = self._rem_nth(head, n)
        return new_head
    
    def _rem_nth(self, node, n):
        if node is None:
            return 0, node
        dst, nxt = self._rem_nth(node.next, n)
        node.next = nxt
        if dst + 1 == n:
            return dst + 1, node.next
        return dst + 1, node
        
