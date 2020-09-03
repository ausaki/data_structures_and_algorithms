# title: maximum-level-sum-of-a-binary-tree
# detail: https://leetcode.com/submissions/detail/375316219/
# datetime: Mon Aug  3 15:28:09 2020
# runtime: 316 ms
# memory: 17.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q = collections.deque()
        q.append(root)
        result = -1
        level = 1
        max_sum = -(10 ** 5) - 1
        
        while q:
            s = 0
            for i in range(len(q)):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s > max_sum:
                max_sum = s
                result = level
            level += 1
        return result