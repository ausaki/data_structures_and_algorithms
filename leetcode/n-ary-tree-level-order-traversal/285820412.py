# title: n-ary-tree-level-order-traversal
# detail: https://leetcode.com/submissions/detail/285820412/
# datetime: Sat Dec 14 12:54:48 2019
# runtime: 40 ms
# memory: 14.6 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        curr = collections.deque()
        if root:
            curr.append(root)
        while curr:
            values = []
            for i in range(len(curr)):
                node = curr.popleft()
                values.append(node.val)
                for child in node.children:
                    curr.append(child)
            res.append(values)
        return res