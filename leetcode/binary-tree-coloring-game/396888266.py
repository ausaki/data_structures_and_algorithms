# title: binary-tree-coloring-game
# detail: https://leetcode.com/submissions/detail/396888266/
# datetime: Thu Sep 17 13:02:31 2020
# runtime: 44 ms
# memory: 13.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def visit(root):
            nonlocal result
            if root is None:
                return 0
            l = visit(root.left)
            r = visit(root.right)
            val = l + r + 1
            if root.val == x:
                result = l > n - l or r > n - r or n - val > val
            root.val = val
            return val
        result = False
        visit(root)
        return result