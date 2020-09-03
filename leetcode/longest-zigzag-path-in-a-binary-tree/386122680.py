# title: longest-zigzag-path-in-a-binary-tree
# detail: https://leetcode.com/submissions/detail/386122680/
# datetime: Tue Aug 25 19:13:56 2020
# runtime: 568 ms
# memory: 62.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        result = 0
        def visit(root):
            nonlocal result
            if root is None:
                return -1, -1
            l1, l2 = visit(root.left)
            r1, r2 = visit(root.right)
            l = 1 + l2
            r = 1 + r1
            result = max(result, l, r)
            return l, r
        
        visit(root)
        return result