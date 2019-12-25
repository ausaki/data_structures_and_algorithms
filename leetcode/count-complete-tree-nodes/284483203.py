# title: count-complete-tree-nodes
# detail: https://leetcode.com/submissions/detail/284483203/
# datetime: Sun Dec  8 13:16:55 2019
# runtime: 80 ms
# memory: 20 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def _dfs(node, h):
            if node.left is None:
                return h, 1, False
            h1, n, f = _dfs(node.left, h + 1)
            if f:
                return h1, n, f
            if node.right is None:
                return h1, n, True                
            h2, m, f = _dfs(node.right, h + 1)
            if h2 == h1:
                return h1, n + m, f
            return h1, n, True
                
        if root is None:
            return 0
        mh, n, _ = _dfs(root, 0)
        return 2 ** mh - 1 + n
                    
            
                