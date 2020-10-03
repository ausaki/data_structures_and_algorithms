# title: cousins-in-binary-tree
# detail: https://leetcode.com/submissions/detail/401708986/
# datetime: Mon Sep 28 14:31:57 2020
# runtime: 24 ms
# memory: 14.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        u = [-1, -1]
        v = [-1, -1]
        def dfs(root, d, p):
            if root is None:
                return 
            if u[0] != -1 and v[0] != -1:
                return
            if root.val == x:
                v[0] = d
                v[1] = p
                return
            if root.val == y:
                u[0] = d
                u[1] = p
                return
            dfs(root.left, d + 1, root.val)
            dfs(root.right, d + 1, root.val)
        dfs(root, 0, -1)
        return u[0] == v[0] and u[1] != v[1]