# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        list_len = 0
        counter = root
        while counter:
            counter = counter.next
            list_len += 1
        
        part_size = list_len / k
        larger = list_len - (part_size * k)
        ret = [root]
        for part in xrange(k - 1):
            new_root = ret[part]
            prev = None
            for c in xrange(part_size + int(part < larger)):
                if not new_root:
                    break
                prev = new_root
                new_root = new_root.next
            if prev:
                prev.next = None
            ret.append(new_root)
        return ret
        
