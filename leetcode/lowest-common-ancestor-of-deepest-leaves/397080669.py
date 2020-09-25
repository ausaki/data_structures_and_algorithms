# title: lowest-common-ancestor-of-deepest-leaves
# detail: https://leetcode.com/submissions/detail/397080669/
# datetime: Fri Sep 18 00:04:06 2020
# runtime: 60 ms
# memory: 14.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def visit(root, h):
            if root is None:
                return h, None
            l, a = visit(root.left, h + 1)
            r, b = visit(root.right, h + 1)
            if l == r:
                return l, root
            if l < r:
                return r, b
            return l, a
        h, a = visit(root, 0)
        return a