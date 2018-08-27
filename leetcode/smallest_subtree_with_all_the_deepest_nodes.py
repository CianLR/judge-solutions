# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        max_dep = 0
        deeps = []
        new_deeps = [root]
        while new_deeps:
            deeps, new_deeps = new_deeps, []
            for d in deeps:
                if d.left:
                    d.left.parent = d
                    new_deeps.append(d.left)
                if d.right:
                    d.right.parent = d
                    new_deeps.append(d.right)
        
        common = None
        new_common = set(deeps)
        while len(new_common) > 1:
            common, new_common = new_common, set()
            for d in common:
                new_common.add(d.parent)
        return list(new_common)[0]
            
