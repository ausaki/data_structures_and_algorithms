# title: number-of-good-leaf-nodes-pairs
# detail: https://leetcode.com/submissions/detail/376409435/
# datetime: Wed Aug  5 17:17:00 2020
# runtime: 508 ms
# memory: 15.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        result = 0
        
        def dfs(root, h):
            nonlocal result
            if root is None:
                return []
            left = dfs(root.left, h + 1)
            right = dfs(root.right, h + 1)
            for l in left:
                for r in right:
                    if l - h + r - h <= distance:
                        result += 1
            if not left and not right:
                return [h]
            return left + right
        
        dfs(root, 0)
        return result
            