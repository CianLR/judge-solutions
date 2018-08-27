# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten_recur(self, root):
        if root.left is None and root.right is None:
            return root
        if root.right is None:
            root.left, root.right = root.right, root.left
            return self.flatten_recur(root.right)
        if root.left is None:
            return self.flatten_recur(root.right)
        left_end = self.flatten_recur(root.left)
        right_end = self.flatten_recur(root.right)
        root.left, root.right, left_end.right = None, root.left, root.right
        return right_end
        # return end
    
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is not None:
            self.flatten_recur(root)
        
