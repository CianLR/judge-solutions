# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

INF = 10e9


class Solution(object):
    def isValidBST(self, root, lo=-INF, hi=INF):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        return (lo < root.val < hi and
                self.isValidBST(root.left, lo, min(hi, root.val)) and
                self.isValidBST(root.right, max(lo, root.val), hi))
    
        
