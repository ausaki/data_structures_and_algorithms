# title: flatten-a-multilevel-doubly-linked-list
# detail: https://leetcode.com/submissions/detail/285824527/
# datetime: Sat Dec 14 13:23:27 2019
# runtime: 36 ms
# memory: 13.2 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def _flatten(head):
            prev = None
            curr = head
            while curr:
                if curr.child:
                    child = _flatten(curr.child)
                    curr.child = None
                    child.prev.next = curr.next
                    if curr.next:
                        curr.next.prev = child.prev
                    curr.next, child.prev, curr = child, curr, child.prev
                prev, curr = curr, curr.next
            head.prev = prev
            return head
        if head is None:
            return head
        head = _flatten(head)
        head.prev = None
        return head