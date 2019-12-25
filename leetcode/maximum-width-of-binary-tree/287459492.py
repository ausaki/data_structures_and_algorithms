# title: maximum-width-of-binary-tree
# detail: https://leetcode.com/submissions/detail/287459492/
# datetime: Sat Dec 21 12:03:57 2019
# runtime: 36 ms
# memory: 13 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque()
        queue.append((root, 0))
        res = 0
        while queue:
            left = -1
            right = -1
            for i in range(len(queue)):
                node, j = queue.popleft()
                if left < 0:
                    left = j
                right = j
                if node.left:
                    queue.append((node.left, 2 * j + 1))
                if node.right:
                    queue.append((node.right, 2 * j + 2))
            res = max(res, right - left + 1)
        return res