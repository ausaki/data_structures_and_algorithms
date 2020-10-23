# title: even-odd-tree
# detail: https://leetcode.com/submissions/detail/409804399/
# datetime: Sat Oct 17 21:10:54 2020
# runtime: 492 ms
# memory: 40.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        q = collections.deque([root])
        level = 0
        while q:
            parity = level % 2
            prev = -1
            for i in range(len(q)):
                node = q.popleft()
                if node.val % 2 == parity:
                    return False
                if prev >= 1:
                    diff = node.val - prev
                    if diff == 0 or (parity == 1 and diff > 0) or (parity == 0 and diff < 0):
                        return False
                prev = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return True