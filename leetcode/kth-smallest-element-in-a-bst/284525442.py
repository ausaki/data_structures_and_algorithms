# title: kth-smallest-element-in-a-bst
# detail: https://leetcode.com/submissions/detail/284525442/
# datetime: Sun Dec  8 17:32:22 2019
# runtime: 40 ms
# memory: 16.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node = root
        stack = []
        res = 0
        while k:
            while node and node.left:
                stack.append(node)
                node = node.left
            if node is None:
                node = stack.pop()
            k -= 1
            if k == 0:
                res = node.val
                break
            node = node.right
        return res
                