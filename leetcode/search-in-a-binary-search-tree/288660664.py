# title: search-in-a-binary-search-tree
# detail: https://leetcode.com/submissions/detail/288660664/
# datetime: Thu Dec 26 16:38:37 2019
# runtime: 80 ms
# memory: 14.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root
        while curr:
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                return curr
        return None