# title: count-complete-tree-nodes
# detail: https://leetcode.com/submissions/detail/284482787/
# datetime: Sun Dec  8 13:14:42 2019
# runtime: 68 ms
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
            if node.left:
                h1, n, f = _dfs(node.left, h + 1)
                if f:
                    return h1, n, f
                if node.right:
                    h2, m, f = _dfs(node.right, h + 1)
                    return h1, n + (m if h2 == h1 else 0), f if h2 == h1 else True
                else:
                    return h1, n, True
            else:
                return h, 1, False
        if root is None:
            return 0
        mh, n, _ = _dfs(root, 0)
        return 2 ** mh - 1 + n
                    
            
                