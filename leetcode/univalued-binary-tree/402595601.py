# title: univalued-binary-tree
# detail: https://leetcode.com/submissions/detail/402595601/
# datetime: Wed Sep 30 15:21:06 2020
# runtime: 28 ms
# memory: 14 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        seen = set()
        def dfs(root):
            if root is None:
                return
            seen.add(root.val)
            dfs(root.left)
            if len(seen) > 1:
                return
            dfs(root.right)
        dfs(root)
        return len(seen) == 1