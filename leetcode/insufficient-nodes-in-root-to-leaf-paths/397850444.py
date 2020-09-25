# title: insufficient-nodes-in-root-to-leaf-paths
# detail: https://leetcode.com/submissions/detail/397850444/
# datetime: Sat Sep 19 21:58:04 2020
# runtime: 184 ms
# memory: 15.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def visit(root, s):
            if root is None:
                return None
            s += root.val
            if root.left is None and root.right is None:
                return None if s < limit else root
            root.right = visit(root.right, s)
            root.left = visit(root.left, s)
            return None if root.left is None and root.right is None else root
        return visit(root, 0)
