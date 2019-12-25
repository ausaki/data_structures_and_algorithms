# title: find-largest-value-in-each-tree-row
# detail: https://leetcode.com/submissions/detail/286782608/
# datetime: Wed Dec 18 11:54:38 2019
# runtime: 48 ms
# memory: 15 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        queue = collections.deque()
        if root:
            queue.append(root)
        res = []
        while queue:
            m = float('-inf')
            for i in range(len(queue)):
                node = queue.popleft()
                if node.val > m:
                    m = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(m)
        return res
            
        