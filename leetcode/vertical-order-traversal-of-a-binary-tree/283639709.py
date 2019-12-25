# title: vertical-order-traversal-of-a-binary-tree
# detail: https://leetcode.com/submissions/detail/283639709/
# datetime: Wed Dec  4 15:52:37 2019
# runtime: 28 ms
# memory: 12.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        neg = []
        pos = []
        
        q = deque()
        q.append((0, 0, root))
        curr_y = 0
        while q:
            tmp = []
            while q and q[0][1] == curr_y:
                x, y, node = q.popleft()
                tmp.append((x, node.val))
                if node.left:
                    q.append((x - 1, y - 1, node.left))
                if node.right:
                    q.append((x + 1, y - 1, node.right))
            curr_y -= 1
            tmp = sorted(tmp)
            for x, val in tmp:
                if x >= 0:
                    if x == len(pos):
                        pos.append([])
                    pos[x].append(val)
                if x < 0:
                    if -x - 1 == len(neg):
                        neg.append([])
                    neg[-x - 1].append(val)
        return neg[::-1] + pos