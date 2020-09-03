# title: maximum-sum-bst-in-binary-tree
# detail: https://leetcode.com/submissions/detail/386129162/
# datetime: Tue Aug 25 19:40:56 2020
# runtime: 688 ms
# memory: 67.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        def visit(root):
            nonlocal result
            ls, lb, lmi, lma = 0, True, root.val, -1e5
            rs, rb, rmi, rma = 0, True, 1e5, root.val
            if root.left:
                ls, lb, lmi, lma = visit(root.left)
            if root.right:
                rs, rb, rmi, rma = visit(root.right)
            if lb and rb and  lma < root.val < rmi:
                s = ls + rs + root.val
                result = max(result, s)
                return s, True, lmi, rma
            return 0, False, 0, 0
        
        result = 0
        visit(root)
        return result