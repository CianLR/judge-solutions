# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        level = [root]
        while level:
            new_level = []
            for i in range(len(level)):
                if level[i].left is not None:
                    new_level.append(level[i].left)
                if level[i].right is not None:
                    new_level.append(level[i].right)
                if i > 0:
                    level[i - 1].next = level[i]
            level = new_level
        
