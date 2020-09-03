# title: number-of-good-leaf-nodes-pairs
# detail: https://leetcode.com/submissions/detail/376415171/
# datetime: Wed Aug  5 17:38:49 2020
# runtime: 172 ms
# memory: 15.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        result = 0
        
        def merge(arr1, arr2):
            arr = []
            
        def dfs(root, h):
            nonlocal result
            if root is None:
                return []
            left = dfs(root.left, h + 1)
            right = dfs(root.right, h + 1)
            for l in left:
                if l - h >= distance:
                    break
                for r in right:
                    if l - h + r - h <= distance:
                        result += 1
                    else:
                        break
            if not left and not right:
                return [h]
            return list(heapq.merge(left, right))
        
        dfs(root, 0)
        return result
            