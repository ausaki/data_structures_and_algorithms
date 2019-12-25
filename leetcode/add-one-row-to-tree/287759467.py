# title: add-one-row-to-tree
# detail: https://leetcode.com/submissions/detail/287759467/
# datetime: Sun Dec 22 22:57:13 2019
# runtime: 52 ms
# memory: 15.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def add(root, depth):
            if root is None:
                return
            if depth < d - 1:
                add(root.left, depth + 1)
                add(root.right, depth + 1)
                return
            left = TreeNode(v)
            right = TreeNode(v)
            left.left = root.left
            right.right = root.right
            root.left = left
            root.right = right
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        add(root, 1)
        return root