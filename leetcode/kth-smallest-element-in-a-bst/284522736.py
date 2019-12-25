# title: kth-smallest-element-in-a-bst
# detail: https://leetcode.com/submissions/detail/284522736/
# datetime: Sun Dec  8 17:09:30 2019
# runtime: 44 ms
# memory: 16.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def dfs(node, i):
            if node is None:
                return None, i
            v, j = dfs(node.left, i)
            if v is not None:
                return v, j
            i = j + 1
            if i == k - 1:
                return node.val, i
            v, j = dfs(node.right, i) 
            return v, j
        v, _ = dfs(root, -1)
        return v
                