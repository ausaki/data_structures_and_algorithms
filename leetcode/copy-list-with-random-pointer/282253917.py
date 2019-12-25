# title: copy-list-with-random-pointer
# detail: https://leetcode.com/submissions/detail/282253917/
# datetime: Thu Nov 28 17:50:50 2019
# runtime: 40 ms
# memory: 14.9 MB

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
        
        def _copy2(node):
            if node is None:
                return None
            old = node
            while old:
                new = Node(old.val, old.next, None)
                old.next = new
                old = new.next
            old = node
            while old:
                new = old.next
                new.random = old.random.next if old.random else None
                old = new.next
            old = node
            new_head = node.next
            while old:
                new = old.next
                old.next = old.next.next
                new.next = new.next.next if new.next else None
                old = old.next
            return new_head
        seen = {}
        return _copy2(head)