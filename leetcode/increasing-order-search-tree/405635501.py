# title: increasing-order-search-tree
# detail: https://leetcode.com/submissions/detail/405635501/
# datetime: Wed Oct  7 16:41:45 2020
# runtime: 28 ms
# memory: 14 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if root is None:
                return None, None
            head, tail = dfs(root.left)
            if tail:
                tail.right = root
            head1, tail1 = dfs(root.right)
            root.left = None
            root.right = head1
            return head if head else root, tail1 if tail1 else root
        
        h, t = dfs(root)
        return h