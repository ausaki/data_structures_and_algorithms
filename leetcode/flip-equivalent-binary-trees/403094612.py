# title: flip-equivalent-binary-trees
# detail: https://leetcode.com/submissions/detail/403094612/
# datetime: Thu Oct  1 20:49:07 2020
# runtime: 28 ms
# memory: 14.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None:
            return root2 is None
        if root2 is None:
            return False
        if root1.val != root2.val:
            return False
        l1 = root1.left.val if root1.left else -1
        l2 = root2.left.val if root2.left else -1
        if l1 != l2:
            root1.left, root1.right = root1.right, root1.left
        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            
        