# title: construct-binary-tree-from-preorder-and-postorder-traversal
# detail: https://leetcode.com/submissions/detail/405991786/
# datetime: Thu Oct  8 12:29:08 2020
# runtime: 44 ms
# memory: 14.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def build(i, j, l):
            if l <= 0:
                return None
            root = TreeNode(pre[i])
            if l == 1:
                return root
            k = post.index(pre[i + 1], j, j + l)
            root.left = build(i + 1, j, k - j + 1)
            root.right = build(i + k - j + 2, k + 1, j + l - k - 2)
            return root
        return build(0, 0, len(pre))