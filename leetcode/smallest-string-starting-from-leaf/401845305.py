# title: smallest-string-starting-from-leaf
# detail: https://leetcode.com/submissions/detail/401845305/
# datetime: Mon Sep 28 23:31:08 2020
# runtime: 48 ms
# memory: 15.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(root):
            nonlocal result
            path.append(root.val)
            if root.left is None and root.right is None:
                result = min(result, path[::-1])
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            path.pop()
        result = [26]
        path = []
        dfs(root)
        return ''.join(chr(97 + i) for i in result)
            
            