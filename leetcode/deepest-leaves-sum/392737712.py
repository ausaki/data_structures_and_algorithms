# title: deepest-leaves-sum
# detail: https://leetcode.com/submissions/detail/392737712/
# datetime: Tue Sep  8 16:32:28 2020
# runtime: 96 ms
# memory: 17.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        s = 0
        height = 0
        def dfs(root, h):
            nonlocal s, height
            if root is None:
                return
            if root.left is None and root.right is None:
                if h < height:
                    return
                if h == height:
                    s += root.val
                    return
                height = h
                s = root.val
            else:
                dfs(root.left, h + 1)
                dfs(root.right, h + 1)
        dfs(root, 0)
        return s