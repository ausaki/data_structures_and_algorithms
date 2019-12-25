# title: flatten-binary-tree-to-linked-list
# detail: https://leetcode.com/submissions/detail/148114168/
# datetime: Mon Apr  2 14:46:48 2018
# runtime: 49 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _flatten(self, root, prev):
        if root is None:
            return prev
        if prev is None:
            prev = root
        else:
            prev.left = None
            prev.right = root
            prev = root
        right = root.right
        prev = self._flatten(root.left, prev)
        prev = self._flatten(right, prev)
        return prev
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self._flatten(root, None)
        