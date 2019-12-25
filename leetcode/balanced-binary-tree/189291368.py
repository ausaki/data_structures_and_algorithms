# title: balanced-binary-tree
# detail: https://leetcode.com/submissions/detail/189291368/
# datetime: Tue Nov 13 16:26:11 2018
# runtime: 44 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _isBalanced(self, root):
        if root is None:
            return 0
        left_depth = self._isBalanced(root.left)
        right_depth = self._isBalanced(root.right)
        
        if left_depth == -1 or right_depth == -1:
            return -1
        
        if abs(left_depth - right_depth) > 1:
            return -1
        
        return max(left_depth, right_depth) + 1
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        depth = self._isBalanced(root)
        if depth == -1:
            return False
        else:
            return True
        