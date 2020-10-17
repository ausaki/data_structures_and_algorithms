# title: leaf-similar-trees
# detail: https://leetcode.com/submissions/detail/406529823/
# datetime: Fri Oct  9 18:57:44 2020
# runtime: 28 ms
# memory: 14.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def inorder(root, leaves):
            if root.left is None and root.right is None:
                leaves.append(root.val)
                return
            if root.left:
                inorder(root.left, leaves)
            if root.right:
                inorder(root.right, leaves)
        leaves1 = []
        leaves2 = []
        inorder(root1, leaves1)
        inorder(root2, leaves2)
        return leaves1 == leaves2
                