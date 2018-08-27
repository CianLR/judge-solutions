# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dumb = ListNode(None)
        dumb.next = head
        start = dumb
        middle = dumb.next
        if middle is None:
            return head
        end = middle.next
        if end is None:
            return head
        while True:
            start.next, end.next, middle.next = end, middle, end.next
            start = middle
            if start.next is None:
                break
            middle = start.next
            if middle.next is None:
                break
            end = middle.next
        return dumb.next
        
