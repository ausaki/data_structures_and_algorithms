# title: number-of-good-leaf-nodes-pairs
# detail: https://leetcode.com/submissions/detail/376416955/
# datetime: Wed Aug  5 17:45:55 2020
# runtime: 172 ms
# memory: 15 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
import bisect

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
                if l - h >= distance:
                    break
                i = bisect.bisect(right, distance - (l - 2 * h))
                result += i
            if not left and not right:
                return [h]
            return list(heapq.merge(left, right))
        
        dfs(root, 0)
        return result
            