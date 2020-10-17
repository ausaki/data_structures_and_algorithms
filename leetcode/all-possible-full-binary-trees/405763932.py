# title: all-possible-full-binary-trees
# detail: https://leetcode.com/submissions/detail/405763932/
# datetime: Thu Oct  8 00:36:07 2020
# runtime: 184 ms
# memory: 16.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        @lru_cache(None)
        def build(n):
            if n == 1:
                return [TreeNode()]
            trees = []
            for i in range(1, n - 1, 2):
                left_trees = build(i)
                right_trees = build(n - i - 1)
                for l in left_trees:
                    for r in right_trees:
                        trees.append(TreeNode(0, l, r))
            return trees
        if N % 2 == 0:
            return []
        return build(N)