# title: binary-tree-preorder-traversal
# detail: https://leetcode.com/submissions/detail/284119943/
# datetime: Fri Dec  6 18:53:32 2019
# runtime: 40 ms
# memory: 12.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # def traverse(node):
        #     if node is None:
        #         return
        #     res.append(node.val)
        #     traverse(node.left)
        #     traverse(node.right)
        # res = []
        # traverse(root)
        # return res
        
        res = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if node is None:
                continue
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res