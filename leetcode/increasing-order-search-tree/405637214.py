# title: increasing-order-search-tree
# detail: https://leetcode.com/submissions/detail/405637214/
# datetime: Wed Oct  7 16:48:05 2020
# runtime: 32 ms
# memory: 14.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head, curr = None, None
        def dfs(root):
            nonlocal head, curr
            if root is None:
                return
            dfs(root.left)
            if curr is None:
                head = curr = root
            else:
                curr.right = root
                root.left = None
                curr = root
            dfs(root.right)
        
        dfs(root)
        return head