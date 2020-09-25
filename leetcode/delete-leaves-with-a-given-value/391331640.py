# title: delete-leaves-with-a-given-value
# detail: https://leetcode.com/submissions/detail/391331640/
# datetime: Sat Sep  5 22:05:37 2020
# runtime: 52 ms
# memory: 14.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def remove(root):
            if root is None:
                return True
            l = remove(root.left)
            if l:
                root.left = None
            r = remove(root.right)
            if r:
                root.right = None
            return l and r and root.val == target
        if remove(root):
            return None
        return root