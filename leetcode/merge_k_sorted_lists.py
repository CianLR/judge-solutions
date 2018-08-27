# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = []
        for lst in lists:
            while lst:
                l.append(lst.val)
                lst = lst.next
        l = sorted(l, reverse=True)
        prev = None
        for c in l:
            node = ListNode(c)
            node.next = prev
            prev = node
        return prev
        
