# title: pseudo-palindromic-paths-in-a-binary-tree
# detail: https://leetcode.com/submissions/detail/381734078/
# datetime: Sun Aug 16 22:05:01 2020
# runtime: 384 ms
# memory: 49.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def bitcount(n):
            cnt = 0
            while n:
                n &= n - 1
                cnt += 1
            return cnt
        
        def visit(root, bits):
            if root is None:
                return 1 if bitcount(bits) <= 1 else 0
            bits ^= 1 << root.val
            if root.left is None:
                return visit(root.right, bits)
            if root.right is None:
                return visit(root.left, bits)
            return visit(root.left, bits) + visit(root.right, bits)
        
        return visit(root, 0)