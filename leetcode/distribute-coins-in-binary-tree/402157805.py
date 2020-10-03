# title: distribute-coins-in-binary-tree
# detail: https://leetcode.com/submissions/detail/402157805/
# datetime: Tue Sep 29 15:01:17 2020
# runtime: 36 ms
# memory: 14 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        moves = [0]
        def dfs(root):
            if root is None: return 0
            l = dfs(root.left)
            r = dfs(root.right)
            v = root.val + l + r - 1
            moves[0] += abs(v)
            return v
        dfs(root)
        return moves[0]