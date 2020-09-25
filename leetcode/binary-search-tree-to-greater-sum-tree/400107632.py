# title: binary-search-tree-to-greater-sum-tree
# detail: https://leetcode.com/submissions/detail/400107632/
# datetime: Thu Sep 24 20:25:36 2020
# runtime: 40 ms
# memory: 13.8 MB

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
            v = root.val
            root.val += s + r
            l = dfs(root.left, root.val)
            return l + r + v
        dfs(root, 0)
        return root