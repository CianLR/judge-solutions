# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        zigzag = []
        stack = [root]
        while stack:
            new_zig = []
            new_stack = []
            zigzag.append(new_zig)
            for u in stack:
                if u is None:
                    continue
                new_zig.append(u.val)
                if len(zigzag) % 2 == 0:
                    new_stack.append(u.right)
                    new_stack.append(u.left)
                else:
                    new_stack.append(u.left)
                    new_stack.append(u.right)
            stack = new_stack[::-1]
        if zigzag[-1] == []:
            zigzag = zigzag[:-1]
        return zigzag


