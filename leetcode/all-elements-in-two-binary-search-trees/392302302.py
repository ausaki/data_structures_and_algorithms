# title: all-elements-in-two-binary-search-trees
# detail: https://leetcode.com/submissions/detail/392302302/
# datetime: Mon Sep  7 21:57:26 2020
# runtime: 384 ms
# memory: 21.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def travel(root, data):
            if root is None:
                return
            travel(root.left, data)
            data.append(root.val)
            travel(root.right, data)
        
        data1 = []
        travel(root1, data1)
        data2 = []
        travel(root2, data2)
        return list(heapq.merge(data1, data2))