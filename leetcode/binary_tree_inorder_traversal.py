# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = deque([root])
        trav = []
        while stack:
            u = stack.pop()
            if u is None:
                continue
            if type(u) == int:
                trav.append(u)
            else:
                stack.append(u.right)
                stack.append(u.val)
                stack.append(u.left)
        return trav
        
