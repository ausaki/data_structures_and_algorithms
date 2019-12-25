# title: house-robber-iii
# detail: https://leetcode.com/submissions/detail/284437116/
# datetime: Sun Dec  8 10:20:39 2019
# runtime: 52 ms
# memory: 15.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache
class Solution:
    def rob(self, root: TreeNode) -> int:
        @lru_cache(None)
        def _rob(node):
            if node is None:
                return 0
            n = _rob(node.left) + _rob(node.right)
            m = node.val
            if node.left:
                m += _rob(node.left.left) + _rob(node.left.right)
            if node.right:
                m += _rob(node.right.left) + _rob(node.right.right)
            return max(n, m)
        return _rob(root)