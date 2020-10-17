# title: all-possible-full-binary-trees
# detail: https://leetcode.com/submissions/detail/405767996/
# datetime: Thu Oct  8 00:48:00 2020
# runtime: 184 ms
# memory: 16.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dp = [[TreeNode()]]
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        N //= 2
        for i in range(len(self.dp), N + 1):
            trees = []
            for j in range(i):
                left_trees = self.dp[j]
                right_trees = self.dp[i - 1 - j]
                for l in left_trees:
                    for r in right_trees:
                        trees.append(TreeNode(0, l, r))
            self.dp.append(trees)
        return self.dp[N]
