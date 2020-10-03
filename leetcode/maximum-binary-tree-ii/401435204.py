# title: maximum-binary-tree-ii
# detail: https://leetcode.com/submissions/detail/401435204/
# datetime: Mon Sep 28 00:25:10 2020
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
        curr, parent = root, None
        while curr and curr.val > val:
            curr, parent = curr.right, curr
        if curr is None:
            parent.right = TreeNode(val)
        else:
            node = TreeNode(val, curr)
            if parent:
                parent.right = node
            else:
                root = node
        return root
            
        