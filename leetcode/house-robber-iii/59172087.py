# title: house-robber-iii
# detail: https://leetcode.com/submissions/detail/59172087/
# datetime: Sat Apr 16 15:32:33 2016
# runtime: 104 ms
# memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    cache = {}
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root in self.cache:
            return self.cache[root]
        money1 = 0
        money2 = root.val
        if root.left:
            money1 += self.rob(root.left)
            money2 += self.rob(root.left.left)
            money2 += self.rob(root.left.right)
        if root.right:
            money1 += self.rob(root.right)
            money2 += self.rob(root.right.left)
            money2 += self.rob(root.right.right)
        self.cache[root] = max(money1, money2)
        return self.cache[root]