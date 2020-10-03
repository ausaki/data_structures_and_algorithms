# title: check-completeness-of-a-binary-tree
# detail: https://leetcode.com/submissions/detail/402746416/
# datetime: Thu Oct  1 00:48:30 2020
# runtime: 32 ms
# memory: 14.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = collections.deque([root])
        h = 1
        while q:
            n = len(q)
            for i in range(len(q)):
                node = q.popleft()
                if node is None:
                    return False
                q.append(node.left)
                q.append(node.right)
            while q and q[-1] is None:
                q.pop()
            if n < h and len(q) > 0:
                return False
            h <<= 1
        return True