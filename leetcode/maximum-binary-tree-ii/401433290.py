# title: maximum-binary-tree-ii
# detail: https://leetcode.com/submissions/detail/401433290/
# datetime: Mon Sep 28 00:18:39 2020
# runtime: 32 ms
# memory: 14.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val > root.val:
            root = TreeNode(val, root)
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
        return root