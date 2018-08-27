# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = []
        while l1 and l2:
            if l1.val < l2.val:
                l.append(l1)
                l1 = l1.next
            else:
                l.append(l2)
                l2 = l2.next
        while l1:
            l.append(l1)
            l1 = l1.next
        while l2:
            l.append(l2)
            l2 = l2.next
        for i in range(len(l) - 1):
            l[i].next = l[i + 1]
        return l[0] if len(l) > 0 else None
        
