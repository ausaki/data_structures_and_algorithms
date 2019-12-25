# title: maximum-binary-tree
# detail: https://leetcode.com/submissions/detail/287515319/
# datetime: Sat Dec 21 19:04:06 2019
# runtime: 208 ms
# memory: 13.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def build(i, j):
            if i > j: 
                return None
            m = i
            for k in range(i, j + 1):
                if nums[k] > nums[m]:
                    m = k
            node = TreeNode(nums[m])
            node.left = build(i, m - 1)
            node.right = build(m + 1, j)
            return node
        return build(0, len(nums) - 1)