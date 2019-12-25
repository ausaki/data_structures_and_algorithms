# title: invert-binary-tree
# detail: https://leetcode.com/submissions/detail/194304842/
# datetime: Mon Dec 10 11:59:30 2018
# runtime: 20 ms
# memory: 7 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        l = self.invertTree(root.left)
        r = self.invertTree(root.right)
        root.left, root.right = r, l
        return root
        