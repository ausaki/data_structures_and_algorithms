# title: copy-list-with-random-pointer
# detail: https://leetcode.com/submissions/detail/282248116/
# datetime: Thu Nov 28 17:01:43 2019
# runtime: 44 ms
# memory: 14.8 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def _copy(node):
            if node is None:
                return None
            if node in seen:
                return seen[node]
            copy = Node(node.val, None, None)
            seen[node] = copy
            copy.next = _copy(node.next)
            copy.random = _copy(node.random)
            return copy
        seen = {}
        return _copy(head)