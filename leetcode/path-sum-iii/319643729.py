# title: path-sum-iii
# detail: https://leetcode.com/submissions/detail/319643729/
# datetime: Sun Apr  5 00:13:16 2020
# runtime: 900 ms
# memory: 14.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def count(root, target):
            # target paths starts with root
            if root is None:
                return 0
            v = count(root.left, target - root.val) + count(root.right, target - root.val)
            return v + (1 if target == root.val else 0)
        
        def path(root, target):
            if root is None:
                return 0
            return count(root, target) + path(root.left, target) + path(root.right, target)
        
        return path(root, sum)
