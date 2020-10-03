# title: check-completeness-of-a-binary-tree
# detail: https://leetcode.com/submissions/detail/402748543/
# datetime: Thu Oct  1 00:54:57 2020
# runtime: 32 ms
# memory: 14.1 MB

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
            none = False
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    if none:
                        return False
                    q.append(node.left)
                else:
                    none = True
                if node.right:
                    if none:
                        return False
                    q.append(node.right)
                else:
                    none = True
            if n < h and len(q) > 0:
                return False
            h <<= 1
        return True