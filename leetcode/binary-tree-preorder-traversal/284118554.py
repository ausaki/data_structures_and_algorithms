# title: binary-tree-preorder-traversal
# detail: https://leetcode.com/submissions/detail/284118554/
# datetime: Fri Dec  6 18:37:53 2019
# runtime: 28 ms
# memory: 12.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def traverse(node):
            if node is None:
                return
            res.append(node.val)
            traverse(node.left)
            traverse(node.right)
        res = []
        traverse(root)
        return res
        