# title: binary-tree-cameras
# detail: https://leetcode.com/submissions/detail/402172899/
# datetime: Tue Sep 29 15:48:30 2020
# runtime: 44 ms
# memory: 14.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root):
            if root is None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if l == -1 or r == -1:
                c[0] += 1
                return 1
            if l == 0 and r == 0:
                return -1
            return 0
        c = [0]
        if dfs(root) == -1:
            c[0] += 1
        return c[0]
            
                