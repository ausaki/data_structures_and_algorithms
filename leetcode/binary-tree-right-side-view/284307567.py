# title: binary-tree-right-side-view
# detail: https://leetcode.com/submissions/detail/284307567/
# datetime: Sat Dec  7 19:52:19 2019
# runtime: 32 ms
# memory: 12.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(node, level):
            if node is None:
                return
            if level >= len(res):
                res.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 0)
        return res
                
            