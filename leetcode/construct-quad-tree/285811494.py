# title: construct-quad-tree
# detail: https://leetcode.com/submissions/detail/285811494/
# datetime: Sat Dec 14 11:52:32 2019
# runtime: 152 ms
# memory: 13.7 MB

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(x, y, n):
            if n == 1:
                node = Node(bool(grid[x][y]), True, None, None, None, None)
                return node
            h = n // 2
            tl = dfs(x, y, h)
            tr = dfs(x, y + h, h)
            bl = dfs(x + h, y, h)
            br = dfs(x + h, y + h, h)
            node = None
            if all((tl.isLeaf, tr.isLeaf, bl.isLeaf, br.isLeaf)) and tl.val == tr.val == bl.val == br.val:
                node = Node(tl.val, True, None, None, None, None)
            else:
                node = Node(True, False, tl, tr, bl, br)
            return node
        
        return dfs(0, 0, len(grid))