# title: lowest-common-ancestor-of-a-binary-tree
# detail: https://leetcode.com/submissions/detail/317855380/
# datetime: Wed Apr  1 00:13:01 2020
# runtime: 68 ms
# memory: 24.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q) if root.left else None
        r = self.lowestCommonAncestor(root.right, p, q) if root.right else None
        if l and r:
            return root
        if l:
            return l
        return r
        