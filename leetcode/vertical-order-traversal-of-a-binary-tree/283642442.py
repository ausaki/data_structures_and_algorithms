# title: vertical-order-traversal-of-a-binary-tree
# detail: https://leetcode.com/submissions/detail/283642442/
# datetime: Wed Dec  4 16:08:18 2019
# runtime: 32 ms
# memory: 13.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def traverse(node, x, y):
            if node is None:
                return
            nodes.append((x, y, node.val))
            traverse(node.left, x - 1, y + 1)
            traverse(node.right, x + 1, y + 1)
                
        nodes = []
        traverse(root, 0, 0)
        nodes.sort()
        res = []
        curr_x = -1000
        group = []
        for x, y, val in nodes:
            if x == curr_x:
                group.append(val)
            else:
                if group:
                    res.append(group)
                curr_x = x
                group = [val]
        if group:
            res.append(group)
        return res
            
        
        