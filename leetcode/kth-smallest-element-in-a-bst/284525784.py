# title: kth-smallest-element-in-a-bst
# detail: https://leetcode.com/submissions/detail/284525784/
# datetime: Sun Dec  8 17:35:22 2019
# runtime: 44 ms
# memory: 16.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while k:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
