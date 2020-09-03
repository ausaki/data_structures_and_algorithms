# title: insert-into-a-binary-search-tree
# detail: https://leetcode.com/submissions/detail/288658600/
# datetime: Thu Dec 26 16:27:03 2019
# runtime: 112 ms
# memory: 15 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root