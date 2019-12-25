# title: house-robber-iii
# detail: https://leetcode.com/submissions/detail/59171609/
# datetime: Sat Apr 16 15:24:17 2016
# runtime: 108 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root, cache={None: 0}):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root not in cache:
            robLeftVal = 0 if root.left is None else self.rob(root.left.left) + self.rob(root.left.right)
            robRightVal = 0 if root.right is None else self.rob(root.right.left) + self.rob(root.right.right)
            cache[root] = max(self.rob(root.left) + self.rob(root.right), root.val + robLeftVal + robRightVal)
        return cache[root]