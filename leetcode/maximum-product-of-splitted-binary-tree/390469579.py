# title: maximum-product-of-splitted-binary-tree
# detail: https://leetcode.com/submissions/detail/390469579/
# datetime: Thu Sep  3 21:40:37 2020
# runtime: 392 ms
# memory: 80.1 MB

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
            root.sum = traval(root.left) + traval(root.right) + root.val
            return root.sum
        
        def cut(root):
            if root is None:
                return 0
            result = 0
            if root.left:
                result = max(result, cut(root.left), root.left.sum * (s - root.left.sum))
            if root.right:
                result = max(result, cut(root.right), root.right.sum * (s - root.right.sum))
            return result
                             
        s = traval(root)
        return cut(root) % MOD
        