# title: count-complete-tree-nodes
# detail: https://leetcode.com/submissions/detail/284484126/
# datetime: Sun Dec  8 13:21:34 2019
# runtime: 80 ms
# memory: 20.1 MB

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
                if h >= mh[0]:
                    mh[0] = h
                    n[0] += 1
                    return False
                else:
                    return True
            f = _dfs(node.left, h + 1)
            if f:
                return f
            if node.right is None:
                return True
            return _dfs(node.right, h + 1)
                
        if root is None:
            return 0
        mh = [-1]
        n = [0]
        _dfs(root, 0)
        return 2 ** mh[0] - 1 + n[0]
                    
            
                