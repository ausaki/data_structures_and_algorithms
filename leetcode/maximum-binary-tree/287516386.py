# title: maximum-binary-tree
# detail: https://leetcode.com/submissions/detail/287516386/
# datetime: Sat Dec 21 19:16:16 2019
# runtime: 200 ms
# memory: 13.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def build(left, right, k=-1):
            if left > right: 
                return None
            p = -1
            m = -1
            if k == -1:
                p = left
                m = left
                for i in range(left, right + 1):
                    if nums[i] > nums[m]:
                        p = m
                        m = i
            else:
                m = k
                p = -1
            node = TreeNode(nums[m])
            node.left = build(left, m - 1, p)
            node.right = build(m + 1, right)
            return node
        return build(0, len(nums) - 1)