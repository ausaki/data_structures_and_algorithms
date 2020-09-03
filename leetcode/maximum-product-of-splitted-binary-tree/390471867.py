# title: maximum-product-of-splitted-binary-tree
# detail: https://leetcode.com/submissions/detail/390471867/
# datetime: Thu Sep  3 21:48:12 2020
# runtime: 324 ms
# memory: 76.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        MOD = 10 ** 9 + 7
        
        def traval(root):
            if root is None:
                return 0
            s = traval(root.left) + traval(root.right) + root.val
            subsum.append(s)
            return s

        subsum = []  
        t = traval(root)
        return max(s * (t - s) for s in subsum) % MOD
        