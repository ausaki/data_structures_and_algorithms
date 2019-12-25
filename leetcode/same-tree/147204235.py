# title: same-tree
# detail: https://leetcode.com/submissions/detail/147204235/
# datetime: Tue Mar 27 18:00:12 2018
# runtime: 34 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        
        if p and q:
            if p.val != q.val:
                return False
        else:
            return False
        
        r1 = self.isSameTree(p.left, q.left)
        r2 = self.isSameTree(p.right, q.right)
        return r1 and r2
        