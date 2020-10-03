# title: flip-binary-tree-to-match-preorder-traversal
# detail: https://leetcode.com/submissions/detail/402538675/
# datetime: Wed Sep 30 12:42:55 2020
# runtime: 32 ms
# memory: 14.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        def dfs(root, i):
            if root is None:
                return i, True
            if root.val != voyage[i]:
                return i, False
            if root.left and root.left.val != voyage[i + 1]:
                if root.right is None:
                    return i, False
                nodes.append(root.val)
                root.left, root.right = root.right, root.left
            i, f = dfs(root.left, i + 1)
            if not f:
                return i, f
            i, f = dfs(root.right, i)
            return i, f
        
        nodes = []
        i, f = dfs(root, 0)
        return nodes if f else [-1]
                