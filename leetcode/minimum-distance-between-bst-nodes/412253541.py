# title: minimum-distance-between-bst-nodes
# detail: https://leetcode.com/submissions/detail/412253541/
# datetime: Fri Oct 23 21:24:44 2020
# runtime: 32 ms
# memory: 14.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def min_diff(root):
            d, mi, ma = math.inf, root.val, root.val
            if root.left is None and root.right is None:
                return d, mi, ma
            if root.left:
                d1, mi1, ma1 = min_diff(root.left)
                d = min(d, d1, root.val - ma1)
                mi = mi1
            if root.right:
                d1, mi1, ma2 = min_diff(root.right)
                d = min(d, d1, mi1 - root.val)
                ma = ma2
            return d, mi, ma
        return min_diff(root)[0]
        
            