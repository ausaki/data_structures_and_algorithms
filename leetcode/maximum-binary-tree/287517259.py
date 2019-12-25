# title: maximum-binary-tree
# detail: https://leetcode.com/submissions/detail/287517259/
# datetime: Sat Dec 21 19:26:43 2019
# runtime: 168 ms
# memory: 13.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        stack = []
        for num in nums:
            node = TreeNode(num)
            left = None
            while stack and num > stack[-1].val:
                left = stack.pop()
            node.left = left
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0] if stack else None