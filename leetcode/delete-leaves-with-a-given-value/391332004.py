# title: delete-leaves-with-a-given-value
# detail: https://leetcode.com/submissions/detail/391332004/
# datetime: Sat Sep  5 22:06:58 2020
# runtime: 56 ms
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
            if remove(root.left):
                root.left = None
            if remove(root.right):
                root.right = None
            return root.left is None and root.right is None and root.val == target
        return None if remove(root) else root