# title: delete-node-in-a-bst
# detail: https://leetcode.com/submissions/detail/286077920/
# datetime: Sun Dec 15 14:35:38 2019
# runtime: 60 ms
# memory: 16.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findmax(self, root):
        if root is None: return
        m = self.findmax(root.right)
        if m is None: return root
        if m == root.right:
            root.right = m.left
            m.left = None
        return m
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return 
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        max_node = self.findmax(root.left)
        if max_node is None:
            return root.right
        if max_node != root.left:
            max_node.left = root.left
        max_node.right = root.right
        return max_node