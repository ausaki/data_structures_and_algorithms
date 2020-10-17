# title: smallest-subtree-with-all-the-deepest-nodes
# detail: https://leetcode.com/submissions/detail/406920465/
# datetime: Sat Oct 10 21:28:52 2020
# runtime: 36 ms
# memory: 14.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root, d):
            if root is None:
                return None, d
            root1, d1 = dfs(root.left, d + 1)
            root2, d2 = dfs(root.right, d + 1)
            if d1 > d2:
                return root1, d1
            if d1 < d2:
                return root2, d2
            return root, d1
        return dfs(root, 0)[0]
