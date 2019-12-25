# title: find-bottom-left-tree-value
# detail: https://leetcode.com/submissions/detail/286783808/
# datetime: Wed Dec 18 11:59:46 2019
# runtime: 56 ms
# memory: 15 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = collections.deque()
        if root:
            queue.append(root)
        res = 0
        while queue:
            res = queue[0].val
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res