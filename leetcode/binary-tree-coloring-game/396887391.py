# title: binary-tree-coloring-game
# detail: https://leetcode.com/submissions/detail/396887391/
# datetime: Thu Sep 17 13:00:06 2020
# runtime: 44 ms
# memory: 13.8 MB

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
            val = 1 + visit(root.left) + visit(root.right)
            if root.val == x:
                l = root.left.val if root.left else 0
                r = root.right.val if root.right else 0
                result = l > n - l or r > n - r or n - val > val
            root.val = val
            return val
        result = False
        visit(root)
        return result