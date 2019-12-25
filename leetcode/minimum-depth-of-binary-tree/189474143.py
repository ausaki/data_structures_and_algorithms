# title: minimum-depth-of-binary-tree
# detail: https://leetcode.com/submissions/detail/189474143/
# datetime: Wed Nov 14 13:50:20 2018
# runtime: 44 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        d1 = self.minDepth(root.left)
        d2 = self.minDepth(root.right)
        if d1 == 0:
            if d2 == 0:
                return 1
            else:
                return d2 + 1
        else:
            if d2 == 0:
                return d1 + 1
            else:
                return min(d1, d2) + 1
        