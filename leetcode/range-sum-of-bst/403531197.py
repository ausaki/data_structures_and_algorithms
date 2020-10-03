# title: range-sum-of-bst
# detail: https://leetcode.com/submissions/detail/403531197/
# datetime: Fri Oct  2 22:03:04 2020
# runtime: 216 ms
# memory: 22.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        if L <= root.val <= R:
            return root.val + self.rangeSumBST(root.right, L, R) + self.rangeSumBST(root.left, L, R)
    