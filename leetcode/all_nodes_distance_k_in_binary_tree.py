# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        graph = defaultdict(list)
        stack = deque([root])
        while stack:
            u = stack.pop()
            if u is None:
                continue
            if u.left is not None:
                stack.append(u.left)
                graph[u.val].append(u.left.val)
                graph[u.left.val].append(u.val)
            if u.right is not None:
                stack.append(u.right)
                graph[u.val].append(u.right.val)
                graph[u.right.val].append(u.val)
        queue = deque([(K, target.val)])
        seen = {target.val}
        ret = []
        while queue:
            d, u = queue.popleft()
            if d == 0:
                ret.append(u)
                continue
            for v in graph[u]:
                if v in seen:
                    continue
                seen.add(v)
                queue.append((d - 1, v))
        return ret
                
        
