# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            if carry:
                return ListNode(carry)
            return None
        n = ListNode(0)
        v = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        n.val = v % 10
        n.next = self.addTwoNumbers((l1.next if l1 else None),
                                    (l2.next if l2 else None),
                                    v / 10)
        return n
        
