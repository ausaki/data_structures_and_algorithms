# title: lowest-common-ancestor-of-a-binary-tree
# detail: https://leetcode.com/submissions/detail/275049560/
# datetime: Fri Nov  1 17:04:00 2019
# runtime: 88 ms
# memory: 26.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left is None:
            if right is None:
                return None
            return right
        if right is None:
            return left
        return root
            
        