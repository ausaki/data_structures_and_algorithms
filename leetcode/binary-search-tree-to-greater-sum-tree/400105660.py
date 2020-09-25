# title: binary-search-tree-to-greater-sum-tree
# detail: https://leetcode.com/submissions/detail/400105660/
# datetime: Thu Sep 24 20:17:24 2020
# runtime: 40 ms
# memory: 13.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root, s):
            if root is None:
                return 0
            r = dfs(root.right, s)
            s += r + root.val
            l = dfs(root.left, s)
            s, root.val = l + r + root.val, s
            return s
        dfs(root, 0)
        return root