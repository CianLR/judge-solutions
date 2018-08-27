# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.get_leaves(root1) == self.get_leaves(root2)
    
    def get_leaves(self, root):
        if root is None:
            return ()
        if root.left is None and root.right is None:
            return (root.val,)
        leaves = ()
        if root.left:
            leaves += self.get_leaves(root.left)
        if root.right:
            leaves += self.get_leaves(root.right)
        return leaves
        
