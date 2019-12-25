# title: sum-root-to-leaf-numbers
# detail: https://leetcode.com/submissions/detail/283882451/
# datetime: Thu Dec  5 16:31:55 2019
# runtime: 24 ms
# memory: 12.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, val):
            v = val * 10 + node.val
            res = 0
            if node.left:
                res += dfs(node.left, v)
            if node.right:
                res += dfs(node.right, v)
            return res if res else v
        if root is None:
            return 0
        return dfs(root, 0)