# title: sum-of-nodes-with-even-valued-grandparent
# detail: https://leetcode.com/submissions/detail/391876542/
# datetime: Sun Sep  6 23:57:22 2020
# runtime: 100 ms
# memory: 17.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def travel(root, parent, grandparent):
            if root is None:
                return 0
            s = 0
            if grandparent:
                s += root.val
            parent, grandparent = root.val % 2 == 0, parent
            s += travel(root.left, parent, grandparent)
            s += travel(root.right, parent, grandparent)
            return s
        
        return travel(root, False, False)
        