# title: find-bottom-left-tree-value
# detail: https://leetcode.com/submissions/detail/286785726/
# datetime: Wed Dec 18 12:08:13 2019
# runtime: 40 ms
# memory: 15 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = collections.deque([root])
        node = None
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val